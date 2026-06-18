from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator, Iterator, Mapping
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from enum import Enum
from http import HTTPStatus
import importlib
import inspect
import random
import time
from typing import Any, Generic, TypeVar, get_args, get_origin, get_type_hints

import httpx

from ._operations import OPERATIONS, OperationMetadata
from ._version import __version__
from .client import AuthenticatedClient as RawClient
from .errors import NadeshikoError
from .types import UNSET, Unset

T = TypeVar("T")
RETRYABLE_STATUS = {408, 429, 500, 502, 503, 504}
ENVIRONMENTS = {
    "LOCAL": "http://localhost:5000/api",
    "DEVELOPMENT": "https://api-stg.nadeshiko.co",
    "STAGING": "https://api-stg.nadeshiko.co",
    "PRODUCTION": "https://api.nadeshiko.co",
}


@dataclass(slots=True)
class RetryOptions:
    max_retries: int = 2
    initial_delay: float = 0.5
    max_delay: float = 30.0
    timeout: float | httpx.Timeout | None = None


@dataclass(slots=True)
class SDKResponse(Generic[T]):
    response: httpx.Response
    data: T | None = None
    error: NadeshikoError | None = None

    @property
    def request(self) -> httpx.Request:
        return self.response.request


def _parse_retry_after(value: str | None) -> float:
    if not value:
        return 1.0
    try:
        return max(0.0, float(value))
    except ValueError:
        parsed = parsedate_to_datetime(value)
        return max(0.0, parsed.timestamp() - time.time())


def _backoff_delay(attempt: int, initial_delay: float, max_delay: float) -> float:
    return min(initial_delay * (2**attempt) + random.random() * 0.1, max_delay)


class _RetryingClient(httpx.Client):
    def __init__(self, *args: Any, retry_options: RetryOptions, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._retry_options = retry_options

    def request(self, method: str, url: str, *args: Any, **kwargs: Any) -> httpx.Response:
        attempt = 0
        while True:
            try:
                response = super().request(method, url, *args, **kwargs)
            except httpx.RequestError:
                if attempt >= self._retry_options.max_retries:
                    raise
                time.sleep(
                    _backoff_delay(
                        attempt,
                        self._retry_options.initial_delay,
                        self._retry_options.max_delay,
                    )
                )
                attempt += 1
                continue

            if (
                response.status_code not in RETRYABLE_STATUS
                or attempt >= self._retry_options.max_retries
            ):
                return response

            wait_time = response.headers.get("Retry-After")
            response.close()
            time.sleep(
                _parse_retry_after(wait_time)
                if wait_time is not None
                else _backoff_delay(
                    attempt,
                    self._retry_options.initial_delay,
                    self._retry_options.max_delay,
                )
            )
            attempt += 1


class _RetryingAsyncClient(httpx.AsyncClient):
    def __init__(self, *args: Any, retry_options: RetryOptions, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._retry_options = retry_options

    async def request(
        self, method: str, url: str, *args: Any, **kwargs: Any
    ) -> httpx.Response:
        attempt = 0
        while True:
            try:
                response = await super().request(method, url, *args, **kwargs)
            except httpx.RequestError:
                if attempt >= self._retry_options.max_retries:
                    raise
                await asyncio.sleep(
                    _backoff_delay(
                        attempt,
                        self._retry_options.initial_delay,
                        self._retry_options.max_delay,
                    )
                )
                attempt += 1
                continue

            if (
                response.status_code not in RETRYABLE_STATUS
                or attempt >= self._retry_options.max_retries
            ):
                return response

            wait_time = response.headers.get("Retry-After")
            await response.aclose()
            await asyncio.sleep(
                _parse_retry_after(wait_time)
                if wait_time is not None
                else _backoff_delay(
                    attempt,
                    self._retry_options.initial_delay,
                    self._retry_options.max_delay,
                )
            )
            attempt += 1


def _strip_unset(annotation: Any) -> Any:
    if annotation is inspect.Signature.empty:
        return annotation
    origin = get_origin(annotation)
    if origin is None:
        return annotation
    filtered = [arg for arg in get_args(annotation) if arg not in {Unset, type(None)}]
    if len(filtered) == 1:
        return filtered[0]
    return annotation


def _coerce_annotation(value: Any, annotation: Any) -> Any:
    if value is None or value is UNSET or annotation is inspect.Signature.empty:
        return value

    annotation = _strip_unset(annotation)
    origin = get_origin(annotation)
    if origin is list and isinstance(value, list):
        inner = _strip_unset(get_args(annotation)[0]) if get_args(annotation) else Any
        return [_coerce_annotation(item, inner) for item in value]

    if (
        inspect.isclass(annotation)
        and issubclass(annotation, Enum)
        and isinstance(value, str)
    ):
        return annotation(value)

    return value


def _coerce_body(body_type: Any, value: Any) -> Any:
    if value is UNSET or value is None:
        return value

    body_type = _strip_unset(body_type)
    if body_type is inspect.Signature.empty:
        return value
    if inspect.isclass(body_type) and isinstance(value, body_type):
        return value
    # If value is a dict of fields and body_type is a model, construct the model
    if (
        isinstance(value, Mapping)
        and inspect.isclass(body_type)
        and hasattr(body_type, "from_dict")
    ):
        # Convert nested model instances to their dict representation
        def convert_nested(v: Any) -> Any:
            if hasattr(v, "to_dict"):
                return v.to_dict()
            if isinstance(v, Mapping):
                return {k: convert_nested(vv) for k, vv in v.items()}
            if isinstance(v, (list, tuple)):
                return [convert_nested(item) for item in v]
            return v
        return body_type.from_dict({k: convert_nested(v) for k, v in value.items()})
    return value


def _coerce_problem_value(value: Any) -> Any:
    if value is UNSET:
        return None
    if isinstance(value, Enum):
        return value.value
    if hasattr(value, "to_dict"):
        return value.to_dict()
    return value


def _error_from_response(response: httpx.Response, parsed: Any) -> NadeshikoError:
    if parsed is not None and hasattr(parsed, "code") and hasattr(parsed, "detail"):
        problem = {
            "code": (
                _coerce_problem_value(getattr(parsed, "code", None))
                or "UNKNOWN_ERROR"
            ),
            "title": (
                _coerce_problem_value(getattr(parsed, "title", None))
                or "Unexpected error"
            ),
            "detail": _coerce_problem_value(getattr(parsed, "detail", None))
            or response.text
            or f"HTTP {response.status_code}",
            "status": _coerce_problem_value(getattr(parsed, "status", None))
            or response.status_code,
            "type": _coerce_problem_value(
                getattr(parsed, "type_", getattr(parsed, "type", None))
            ),
            "instance": _coerce_problem_value(getattr(parsed, "instance", None)),
            "errors": _coerce_problem_value(getattr(parsed, "errors", None)),
        }
        return NadeshikoError.from_problem(problem, response=response)

    try:
        payload = response.json()
    except ValueError:
        payload = None

    if isinstance(payload, Mapping):
        return NadeshikoError.from_problem(payload, response=response)

    return NadeshikoError(
        code="UNKNOWN_ERROR",
        title=HTTPStatus(response.status_code).phrase,
        detail=response.text or f"HTTP {response.status_code}",
        status=response.status_code,
        response=response,
    )


@dataclass(slots=True)
class _LoadedOperation:
    metadata: OperationMetadata
    get_kwargs: Any
    parse_response: Any
    path_params: tuple[str, ...]
    query_params: tuple[str, ...]
    type_hints: dict[str, Any]
    has_body: bool
    body_required: bool


class _ClientBase:
    _operation_cache: dict[str, _LoadedOperation] = {}

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = "PRODUCTION",
        headers: Mapping[str, str] | None = None,
        retry_options: RetryOptions | None = None,
        timeout: float | httpx.Timeout | None = None,
        verify_ssl: bool = True,
        follow_redirects: bool = False,
        httpx_args: Mapping[str, Any] | None = None,
    ) -> None:
        self.retry_options = retry_options or RetryOptions()
        resolved_timeout = timeout if timeout is not None else self.retry_options.timeout
        resolved_base_url = ENVIRONMENTS.get(base_url, base_url)
        base_headers = {"User-Agent": f"nadeshiko-sdk-python/{__version__}"}
        if headers:
            base_headers.update(dict(headers))

        self.client = RawClient(
            base_url=resolved_base_url,
            token=api_key,
            headers={k: str(v) for k, v in base_headers.items()},
            timeout=resolved_timeout,
            verify_ssl=verify_ssl,
            follow_redirects=follow_redirects,
            raise_on_unexpected_status=False,
            httpx_args=dict(httpx_args or {}),
        )

        auth_value = (
            f"{self.client.prefix} {self.client.token}"
            if self.client.prefix
            else self.client.token
        )
        auth_headers = {self.client.auth_header_name: auth_value, **dict(base_headers)}
        client_kwargs = dict(self.client._httpx_args)

        self.client.set_httpx_client(
            _RetryingClient(
                base_url=self.client._base_url,
                cookies=self.client._cookies,
                headers=auth_headers,
                timeout=self.client._timeout,
                verify=self.client._verify_ssl,
                follow_redirects=self.client._follow_redirects,
                retry_options=self.retry_options,
                **client_kwargs,
            )
        )
        self.client.set_async_httpx_client(
            _RetryingAsyncClient(
                base_url=self.client._base_url,
                cookies=self.client._cookies,
                headers=auth_headers,
                timeout=self.client._timeout,
                verify=self.client._verify_ssl,
                follow_redirects=self.client._follow_redirects,
                retry_options=self.retry_options,
                **client_kwargs,
            )
        )

    @classmethod
    def _load_operation(cls, name: str) -> _LoadedOperation:
        cached = cls._operation_cache.get(name)
        if cached is not None:
            return cached

        metadata = next(item for item in OPERATIONS if item.name == name)
        module = importlib.import_module(metadata.module_path, package=__package__)
        signature = inspect.signature(module._get_kwargs)
        type_hints = get_type_hints(module._get_kwargs, module.__dict__, module.__dict__)
        path_params = tuple(
            parameter.name
            for parameter in signature.parameters.values()
            if parameter.kind
            in (parameter.POSITIONAL_ONLY, parameter.POSITIONAL_OR_KEYWORD)
        )
        query_params = tuple(
            parameter.name
            for parameter in signature.parameters.values()
            if parameter.name not in path_params and parameter.name != "body"
        )
        body_parameter = signature.parameters.get("body")
        loaded = _LoadedOperation(
            metadata=metadata,
            get_kwargs=module._get_kwargs,
            parse_response=module._parse_response,
            path_params=path_params,
            query_params=query_params,
            type_hints=type_hints,
            has_body=body_parameter is not None,
            body_required=body_parameter is not None
            and body_parameter.default is inspect.Signature.empty,
        )
        cls._operation_cache[name] = loaded
        return loaded

    def _split_call_arguments(
        self,
        operation: _LoadedOperation,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        path_values: dict[str, Any] = {}
        params = dict(kwargs)

        if operation.path_params:
            if len(args) > len(operation.path_params):
                raise TypeError(
                    f"{operation.metadata.name}() accepts at most "
                    f"{len(operation.path_params)} positional arguments"
                )
            for name, value in zip(operation.path_params, args):
                annotation = operation.type_hints.get(name, inspect.Signature.empty)
                path_values[name] = _coerce_annotation(value, annotation)
            for name in operation.path_params[len(args):]:
                if name not in params:
                    raise TypeError(f"Missing required argument: '{name}'")
                annotation = operation.type_hints.get(name, inspect.Signature.empty)
                path_values[name] = _coerce_annotation(params.pop(name), annotation)
        elif args:
            if len(args) == 1 and hasattr(args[0], "to_dict"):
                # Single model instance passed as positional arg - treat as body
                params = {"body": args[0], **params}
            else:
                raise TypeError(
                    f"{operation.metadata.name}() accepts keyword arguments only"
                )

        return path_values, params

    def _prepare_request_kwargs(
        self,
        operation: _LoadedOperation,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
    ) -> dict[str, Any]:
        path_values, remaining = self._split_call_arguments(operation, args, kwargs)
        request_kwargs = dict(path_values)

        query_values: dict[str, Any] = {}
        for name in operation.query_params:
            if name not in remaining:
                continue
            annotation = operation.type_hints.get(name, inspect.Signature.empty)
            query_values[name] = _coerce_annotation(remaining.pop(name), annotation)
        request_kwargs.update(query_values)

        if operation.has_body:
            body_hint = operation.type_hints.get("body", inspect.Signature.empty)
            if "body" in remaining:
                body = _coerce_body(body_hint, remaining.pop("body"))
            elif remaining or operation.body_required:
                body = _coerce_body(body_hint, remaining)
                remaining = {}
            else:
                body = UNSET

            if body is not UNSET:
                request_kwargs["body"] = body

        if remaining:
            unexpected = ", ".join(sorted(remaining))
            raise TypeError(
                f"Unexpected arguments for {operation.metadata.name}(): {unexpected}"
            )

        return request_kwargs

    def _extract_items(self, page: Any) -> list[Any]:
        attrs = getattr(type(page), "__attrs_attrs__", ())
        for attr in attrs:
            value = getattr(page, attr.name)
            if isinstance(value, list):
                return value
        raise TypeError(
            f"{type(page).__name__} does not expose a paginated list field"
        )

    def _pagination_cursor(self, page: Any) -> str | None:
        pagination = getattr(page, "pagination", None)
        if pagination is None:
            return None
        has_more = getattr(
            pagination, "has_more", getattr(pagination, "hasMore", False)
        )
        cursor = getattr(pagination, "cursor", None)
        if cursor is UNSET:
            cursor = None
        return str(cursor) if has_more and cursor else None

    def _with_cursor(
        self,
        operation: _LoadedOperation,
        kwargs: dict[str, Any],
        cursor: str,
    ) -> dict[str, Any]:
        updated = dict(kwargs)
        if operation.has_body and "body" in updated:
            body = updated["body"]
            if hasattr(body, "to_dict"):
                body_payload = body.to_dict()
            else:
                body_payload = {"cursor": cursor}
            body_payload["cursor"] = cursor
            updated["body"] = body_payload
        else:
            updated["cursor"] = cursor
        return updated

    def close(self) -> None:
        self.client.get_httpx_client().close()

    async def aclose(self) -> None:
        await self.client.get_async_httpx_client().aclose()


class Nadeshiko(_ClientBase):
    def __enter__(self) -> "Nadeshiko":
        self.client.get_httpx_client().__enter__()
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        self.client.get_httpx_client().__exit__(*args, **kwargs)

    def _request(self, operation_name: str, *args: Any, **kwargs: Any) -> Any:
        throw_on_error = kwargs.pop("throw_on_error", True)
        operation = self._load_operation(operation_name)
        request_kwargs = self._prepare_request_kwargs(operation, args, kwargs)
        httpx_kwargs = operation.get_kwargs(**request_kwargs)
        response = self.client.get_httpx_client().request(**httpx_kwargs)
        parsed = operation.parse_response(client=self.client, response=response)

        if 200 <= response.status_code < 300:
            if throw_on_error:
                return parsed
            return SDKResponse(response=response, data=parsed)

        error = _error_from_response(response, parsed)
        if throw_on_error:
            raise error
        return SDKResponse(response=response, error=error)

    def _iterate(self, operation_name: str, *args: Any, **kwargs: Any) -> Iterator[Any]:
        operation = self._load_operation(operation_name)
        if not operation.metadata.paginated:
            raise TypeError(f"{operation_name} is not a paginated endpoint")

        call_kwargs = dict(kwargs)
        while True:
            page = self._request(operation_name, *args, **call_kwargs)
            for item in self._extract_items(page):
                yield item

            cursor = self._pagination_cursor(page)
            if not cursor:
                break
            call_kwargs = self._with_cursor(operation, call_kwargs, cursor)


class AsyncNadeshiko(_ClientBase):
    async def __aenter__(self) -> "AsyncNadeshiko":
        await self.client.get_async_httpx_client().__aenter__()
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        await self.client.get_async_httpx_client().__aexit__(*args, **kwargs)

    async def _request(self, operation_name: str, *args: Any, **kwargs: Any) -> Any:
        throw_on_error = kwargs.pop("throw_on_error", True)
        operation = self._load_operation(operation_name)
        request_kwargs = self._prepare_request_kwargs(operation, args, kwargs)
        httpx_kwargs = operation.get_kwargs(**request_kwargs)
        response = await self.client.get_async_httpx_client().request(**httpx_kwargs)
        parsed = operation.parse_response(client=self.client, response=response)

        if 200 <= response.status_code < 300:
            if throw_on_error:
                return parsed
            return SDKResponse(response=response, data=parsed)

        error = _error_from_response(response, parsed)
        if throw_on_error:
            raise error
        return SDKResponse(response=response, error=error)

    async def _iterate(
        self, operation_name: str, *args: Any, **kwargs: Any
    ) -> AsyncIterator[Any]:
        operation = self._load_operation(operation_name)
        if not operation.metadata.paginated:
            raise TypeError(f"{operation_name} is not a paginated endpoint")

        call_kwargs = dict(kwargs)
        while True:
            page = await self._request(operation_name, *args, **call_kwargs)
            for item in self._extract_items(page):
                yield item

            cursor = self._pagination_cursor(page)
            if not cursor:
                break
            call_kwargs = self._with_cursor(operation, call_kwargs, cursor)


def _make_sync_method(name: str, doc: str) -> Any:
    def method(self: Nadeshiko, *args: Any, **kwargs: Any) -> Any:
        return self._request(name, *args, **kwargs)

    method.__name__ = name
    method.__qualname__ = f"Nadeshiko.{name}"
    method.__doc__ = doc or f"Call the {name} endpoint."
    return method


def _make_sync_iterator(name: str, doc: str) -> Any:
    def method(self: Nadeshiko, *args: Any, **kwargs: Any) -> Iterator[Any]:
        return self._iterate(name, *args, **kwargs)

    method.__name__ = f"iter_{name}"
    method.__qualname__ = f"Nadeshiko.iter_{name}"
    method.__doc__ = doc or f"Iterate through {name} results."
    return method


def _make_async_method(name: str, doc: str) -> Any:
    async def method(self: AsyncNadeshiko, *args: Any, **kwargs: Any) -> Any:
        return await self._request(name, *args, **kwargs)

    method.__name__ = name
    method.__qualname__ = f"AsyncNadeshiko.{name}"
    method.__doc__ = doc or f"Call the {name} endpoint asynchronously."
    return method


def _make_async_iterator(name: str, doc: str) -> Any:
    async def method(self: AsyncNadeshiko, *args: Any, **kwargs: Any) -> AsyncIterator[Any]:
        async for item in self._iterate(name, *args, **kwargs):
            yield item

    method.__name__ = f"iter_{name}"
    method.__qualname__ = f"AsyncNadeshiko.iter_{name}"
    method.__doc__ = doc or f"Iterate through {name} results asynchronously."
    return method


for _operation in OPERATIONS:
    setattr(
        Nadeshiko,
        _operation.name,
        _make_sync_method(_operation.name, _operation.doc),
    )
    setattr(
        AsyncNadeshiko,
        _operation.name,
        _make_async_method(_operation.name, _operation.doc),
    )
    if _operation.paginated:
        setattr(
            Nadeshiko,
            f"iter_{_operation.name}",
            _make_sync_iterator(_operation.name, _operation.doc),
        )
        setattr(
            AsyncNadeshiko,
            f"iter_{_operation.name}",
            _make_async_iterator(_operation.name, _operation.doc),
        )


__all__ = [
    "AsyncNadeshiko",
    "Nadeshiko",
    "RawClient",
    "RetryOptions",
    "SDKResponse",
]
