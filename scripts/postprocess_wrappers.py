from __future__ import annotations

import collections.abc as cabc
import importlib
import inspect
import re
import sys
import textwrap
from contextlib import contextmanager, suppress
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from types import NoneType, UnionType
from typing import Any, Union, get_args, get_origin, get_type_hints

import attrs

HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}


@dataclass(frozen=True)
class WrapperOperation:
    name: str
    module_path: str
    paginated: bool
    doc: str


@dataclass(frozen=True)
class InputField:
    name: str
    annotation: str
    required: bool


@dataclass(frozen=True)
class InputType:
    name: str
    fields: tuple[InputField, ...]


@dataclass(frozen=True)
class StubParameter:
    name: str
    annotation: str
    required: bool
    keyword_only: bool


@dataclass(frozen=True)
class StubOperation:
    name: str
    doc: str
    path_params: tuple[StubParameter, ...]
    keyword_params: tuple[StubParameter, ...]
    response_type: str
    iterator_item_type: str | None


def _operation_id_to_snake(operation_id: str) -> str:
    step_one = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", operation_id)
    step_two = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", step_one)
    return step_two.lower()


def _resolve_ref(spec: dict[str, Any], ref: str) -> Any:
    current: Any = spec
    for part in ref.removeprefix("#/").split("/"):
        current = current[part]
    return current


def _maybe_resolve(spec: dict[str, Any], value: Any) -> Any:
    if isinstance(value, dict) and "$ref" in value:
        return _resolve_ref(spec, value["$ref"])
    return value


def _detect_pagination_in_schema(spec: dict[str, Any], schema: Any) -> bool:
    if not isinstance(schema, dict):
        return False

    properties = schema.get("properties")
    if not isinstance(properties, dict):
        return False

    pagination = properties.get("pagination")
    if not pagination:
        return False

    resolved_pagination = _maybe_resolve(spec, pagination)
    if not isinstance(resolved_pagination, dict):
        return False

    pagination_properties = resolved_pagination.get("properties") or {}
    if not all(key in pagination_properties for key in ("hasMore", "cursor")):
        return False

    return any(
        key != "pagination"
        and isinstance(_maybe_resolve(spec, value), dict)
        and _maybe_resolve(spec, value).get("type") == "array"
        for key, value in properties.items()
    )


def _detect_pagination(spec: dict[str, Any], operation: dict[str, Any]) -> bool:
    if operation.get("x-paginated-items"):
        return True

    response = operation.get("responses", {}).get("200")
    if not response:
        return False

    resolved_response = _maybe_resolve(spec, response)
    schema = resolved_response.get("content", {}).get("application/json", {}).get("schema")
    if not schema:
        return False

    return _detect_pagination_in_schema(spec, _maybe_resolve(spec, schema))


def _find_module_path(package_dir: Path, operation_name: str) -> str | None:
    api_dir = package_dir / "api"
    candidates = sorted(api_dir.rglob(f"{operation_name}.py"))
    if not candidates:
        candidates = sorted(api_dir.rglob(f"{operation_name}_.py"))
    if not candidates:
        return None

    module_path = candidates[0].relative_to(package_dir).with_suffix("")
    return "." + ".".join(module_path.parts)


def collect_operations(spec: dict[str, Any], package_dir: Path) -> list[WrapperOperation]:
    operations: list[WrapperOperation] = []

    for path_item in spec.get("paths", {}).values():
        if not isinstance(path_item, dict):
            continue

        for method, operation in path_item.items():
            if method not in HTTP_METHODS or not isinstance(operation, dict):
                continue

            operation_id = operation.get("operationId")
            if not operation_id:
                continue

            operation_name = _operation_id_to_snake(operation_id)
            module_path = _find_module_path(package_dir, operation_name)
            if module_path is None:
                continue

            description = (operation.get("summary") or operation.get("description") or "").strip()
            operations.append(
                WrapperOperation(
                    name=operation_name,
                    module_path=module_path,
                    paginated=_detect_pagination(spec, operation),
                    doc=description,
                )
            )

    return sorted(operations, key=lambda item: item.name)


@contextmanager
def _package_import_path(package_dir: Path):
    package_parent = str(package_dir.parent)
    sys.path.insert(0, package_parent)
    try:
        yield package_dir.name
    finally:
        with suppress(ValueError):
            sys.path.remove(package_parent)


def _is_union(annotation: Any) -> bool:
    origin = get_origin(annotation)
    return origin in {UnionType, Union}


def _flatten_union(annotation: Any) -> tuple[Any, ...]:
    if _is_union(annotation):
        values: list[Any] = []
        for part in get_args(annotation):
            values.extend(_flatten_union(part))
        return tuple(values)
    return (annotation,)


def _is_unset_type(annotation: Any, unset_type: type[Any]) -> bool:
    return inspect.isclass(annotation) and issubclass(annotation, unset_type)


def _is_attrs_model(annotation: Any) -> bool:
    return inspect.isclass(annotation) and hasattr(annotation, "__attrs_attrs__")


def _is_enum(annotation: Any) -> bool:
    return inspect.isclass(annotation) and issubclass(annotation, Enum)


def _strip_unset(annotation: Any, unset_type: type[Any]) -> tuple[Any, bool]:
    original_parts = _flatten_union(annotation)
    parts = [part for part in original_parts if not _is_unset_type(part, unset_type)]
    is_optional = len(parts) != len(original_parts)
    if not parts:
        return Any, is_optional
    if len(parts) == 1:
        return parts[0], is_optional
    rebuilt = parts[0]
    for part in parts[1:]:
        rebuilt = rebuilt | part
    return rebuilt, is_optional


def _type_sort_key(annotation: Any) -> str:
    if annotation is Any:
        return "Any"
    if annotation is NoneType:
        return "None"
    return getattr(annotation, "__name__", repr(annotation))


def _public_name(name: str) -> str:
    return name[:-1] if name.endswith("_") else name


def _type_to_string(
    annotation: Any,
    *,
    unset_type: type[Any],
    input_types: dict[type[Any], InputType],
    type_namespace: dict[str, Any],
    model_imports: set[str],
    typing_imports: set[str],
) -> str:
    if annotation is Any:
        typing_imports.add("Any")
        return "Any"

    if annotation is NoneType:
        return "None"

    if _is_unset_type(annotation, unset_type):
        typing_imports.add("Any")
        return "Any"

    origin = get_origin(annotation)
    if origin in {UnionType, Union}:
        parts = [_type_to_string(
            part,
            unset_type=unset_type,
            input_types=input_types,
            type_namespace=type_namespace,
            model_imports=model_imports,
            typing_imports=typing_imports,
        ) for part in _flatten_union(annotation) if not _is_unset_type(part, unset_type)]
        unique_parts: list[str] = []
        for part in parts:
            if part not in unique_parts:
                unique_parts.append(part)
        return " | ".join(unique_parts) if unique_parts else "Any"

    if origin in {list, tuple, set, frozenset}:
        inner = get_args(annotation)[0] if get_args(annotation) else Any
        inner_repr = _type_to_string(
            inner,
            unset_type=unset_type,
            input_types=input_types,
            type_namespace=type_namespace,
            model_imports=model_imports,
            typing_imports=typing_imports,
        )
        return f"list[{inner_repr}]"

    if origin in {dict, cabc.Mapping}:
        args = get_args(annotation)
        key_type, value_type = args if len(args) == 2 else (str, Any)
        key_repr = _type_to_string(
            key_type,
            unset_type=unset_type,
            input_types=input_types,
            type_namespace=type_namespace,
            model_imports=model_imports,
            typing_imports=typing_imports,
        )
        value_repr = _type_to_string(
            value_type,
            unset_type=unset_type,
            input_types=input_types,
            type_namespace=type_namespace,
            model_imports=model_imports,
            typing_imports=typing_imports,
        )
        return f"dict[{key_repr}, {value_repr}]"

    if _is_attrs_model(annotation):
        model_name = annotation.__name__
        model_imports.add(model_name)
        return model_name

    if _is_enum(annotation):
        model_imports.add(annotation.__name__)
        return f"{annotation.__name__} | str"

    if inspect.isclass(annotation):
        if annotation.__module__.startswith("builtins"):
            return annotation.__name__
        if annotation.__module__ == "datetime":
            return f"datetime.{annotation.__name__}"
        model_imports.add(annotation.__name__)
        return annotation.__name__

    return repr(annotation).replace("typing.", "")


def _ensure_input_type(
    model_type: type[Any],
    *,
    unset_type: type[Any],
    input_types: dict[type[Any], InputType],
    type_namespace: dict[str, Any],
    model_imports: set[str],
    typing_imports: set[str],
) -> None:
    if model_type in input_types:
        return

    input_types[model_type] = InputType(name=f"{model_type.__name__}Input", fields=())
    module = importlib.import_module(model_type.__module__)
    namespace = type_namespace | module.__dict__

    fields: list[InputField] = []
    for attr in model_type.__attrs_attrs__:
        if attr.name == "additional_properties":
            continue
        annotation = _resolve_annotation(getattr(attr, "type", Any), namespace)
        stripped_annotation, optional_via_unset = _strip_unset(annotation, unset_type)
        field_annotation = _type_to_string(
            stripped_annotation,
            unset_type=unset_type,
            input_types=input_types,
            type_namespace=type_namespace,
            model_imports=model_imports,
            typing_imports=typing_imports,
        )
        required = attr.default is attrs.NOTHING and not optional_via_unset
        fields.append(
            InputField(
                name=_public_name(attr.name),
                annotation=field_annotation,
                required=required,
            )
        )

    input_types[model_type] = InputType(name=f"{model_type.__name__}Input", fields=tuple(fields))


def _resolve_annotation(annotation: Any, namespace: dict[str, Any]) -> Any:
    if isinstance(annotation, str):
        try:
            return eval(annotation, namespace)  # noqa: S307
        except Exception:  # noqa: BLE001
            return Any
    return annotation


def _format_response_type(
    annotation: Any,
    *,
    unset_type: type[Any],
    model_imports: set[str],
    typing_imports: set[str],
) -> str:
    filtered: list[Any] = []
    saw_none = False
    saw_any = False

    for part in _flatten_union(annotation):
        if part is NoneType:
            saw_none = True
            continue
        if part is Any:
            saw_any = True
            continue
        if inspect.isclass(part) and re.fullmatch(r"Error\d+", part.__name__):
            model_imports.add(part.__name__)
            continue
        filtered.append(part)

    if filtered:
        parts = [
            _type_to_string(
                part,
                unset_type=unset_type,
                input_types={},
                type_namespace={},
                model_imports=model_imports,
                typing_imports=typing_imports,
            )
            for part in filtered
        ]
        unique_parts: list[str] = []
        for part in parts:
            if part not in unique_parts:
                unique_parts.append(part)
        return " | ".join(unique_parts)

    if saw_none:
        return "None"
    if saw_any:
        typing_imports.add("Any")
        return "Any"

    typing_imports.add("Any")
    return "Any"


def _extract_iterator_item_type(
    response_annotation: Any,
    *,
    package_name: str,
    type_namespace: dict[str, Any],
    unset_type: type[Any],
    model_imports: set[str],
    typing_imports: set[str],
) -> str | None:
    for part in _flatten_union(response_annotation):
        if not _is_attrs_model(part):
            continue

        module = importlib.import_module(part.__module__)
        namespace = type_namespace | module.__dict__
        for attr in part.__attrs_attrs__:
            annotation = _resolve_annotation(getattr(attr, "type", Any), namespace)
            if get_origin(annotation) is list and get_args(annotation):
                return _type_to_string(
                    get_args(annotation)[0],
                    unset_type=unset_type,
                    input_types={},
                    type_namespace=type_namespace,
                    model_imports=model_imports,
                    typing_imports=typing_imports,
                )
    return None


def collect_stub_data(
    package_dir: Path,
    operations: list[WrapperOperation],
) -> tuple[list[StubOperation], list[InputType], set[str]]:
    stub_operations: list[StubOperation] = []
    input_types: dict[type[Any], InputType] = {}
    stub_model_imports: set[str] = set()
    typing_imports: set[str] = {"Literal", "Generic", "TypeVar", "overload"}

    with _package_import_path(package_dir) as package_name:
        models_module = importlib.import_module(f"{package_name}.models")
        types_module = importlib.import_module(f"{package_name}.types")
        unset_type = types_module.Unset
        type_namespace = dict(models_module.__dict__) | dict(types_module.__dict__)

        for operation in operations:
            module = importlib.import_module(operation.module_path, package=package_name)
            signature = inspect.signature(module._get_kwargs)
            merged_namespace = type_namespace | module.__dict__
            hints = get_type_hints(module._get_kwargs, merged_namespace, merged_namespace)

            path_params: list[StubParameter] = []
            keyword_params: list[StubParameter] = []

            positional_names = [
                parameter.name
                for parameter in signature.parameters.values()
                if parameter.kind in (parameter.POSITIONAL_ONLY, parameter.POSITIONAL_OR_KEYWORD)
            ]

            for parameter in signature.parameters.values():
                if parameter.name == "body":
                    continue

                annotation = hints.get(parameter.name, Any)
                stripped_annotation, optional_via_unset = _strip_unset(annotation, unset_type)
                annotation_repr = _type_to_string(
                    stripped_annotation,
                    unset_type=unset_type,
                    input_types=input_types,
                    type_namespace=type_namespace,
                    model_imports=stub_model_imports,
                    typing_imports=typing_imports,
                )
                required = parameter.default is inspect.Signature.empty and not optional_via_unset
                stub_parameter = StubParameter(
                    name=parameter.name,
                    annotation=annotation_repr,
                    required=required,
                    keyword_only=parameter.name not in positional_names,
                )
                if parameter.name in positional_names:
                    path_params.append(stub_parameter)
                else:
                    keyword_params.append(stub_parameter)

            body_parameter = signature.parameters.get("body")
            if body_parameter is not None:
                body_annotation = hints.get("body", Any)
                stripped_body_annotation, _ = _strip_unset(body_annotation, unset_type)
                if _is_attrs_model(stripped_body_annotation):
                    body_module = importlib.import_module(stripped_body_annotation.__module__)
                    body_namespace = type_namespace | body_module.__dict__
                    for attr in stripped_body_annotation.__attrs_attrs__:
                        if attr.name == "additional_properties":
                            continue
                        attr_annotation = _resolve_annotation(
                            getattr(attr, "type", Any), body_namespace
                        )
                        stripped_annotation, optional_via_unset = _strip_unset(
                            attr_annotation, unset_type
                        )
                        annotation_repr = _type_to_string(
                            stripped_annotation,
                            unset_type=unset_type,
                            input_types=input_types,
                            type_namespace=type_namespace,
                            model_imports=stub_model_imports,
                            typing_imports=typing_imports,
                        )
                        required = attr.default is attrs.NOTHING and not optional_via_unset
                        keyword_params.append(
                            StubParameter(
                                name=_public_name(attr.name),
                                annotation=annotation_repr,
                                required=required,
                                keyword_only=True,
                            )
                        )

            parse_hints = get_type_hints(
                module._parse_response,
                type_namespace | module.__dict__,
                type_namespace | module.__dict__,
            )
            response_annotation = parse_hints.get("return", Any)
            response_type = _format_response_type(
                response_annotation,
                unset_type=unset_type,
                model_imports=stub_model_imports,
                typing_imports=typing_imports,
            )
            iterator_item_type = (
                _extract_iterator_item_type(
                    response_annotation,
                    package_name=package_name,
                    type_namespace=type_namespace,
                    unset_type=unset_type,
                    model_imports=stub_model_imports,
                    typing_imports=typing_imports,
                )
                if operation.paginated
                else None
            )

            stub_operations.append(
                StubOperation(
                    name=operation.name,
                    doc=operation.doc,
                    path_params=tuple(path_params),
                    keyword_params=tuple(keyword_params),
                    response_type=response_type,
                    iterator_item_type=iterator_item_type,
                )
            )

    ordered_input_types = [
        input_types[key] for key in sorted(input_types, key=lambda value: value.__name__)
    ]
    return stub_operations, ordered_input_types, stub_model_imports


def _format_operations_module(operations: list[WrapperOperation]) -> str:
    lines = [
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        "",
        "",
        "@dataclass(frozen=True)",
        "class OperationMetadata:",
        "    name: str",
        "    module_path: str",
        "    paginated: bool = False",
        "    doc: str = ''",
        "",
        "",
        "OPERATIONS: tuple[OperationMetadata, ...] = (",
    ]

    for operation in operations:
        doc = operation.doc.replace('\\', '\\\\').replace('"', '\\"')
        lines.append(
            "    OperationMetadata("
            f"name=\"{operation.name}\", "
            f"module_path=\"{operation.module_path}\", "
            f"paginated={operation.paginated}, "
            f"doc=\"{doc}\""
            "),"
        )

    lines.extend([")", ""])
    return "\n".join(lines)


def _format_errors_module() -> str:
    return textwrap.dedent(
        """\
        \"\"\"Contains shared errors types that can be raised from API functions.\"\"\"

        from __future__ import annotations

        from collections.abc import Mapping
        from typing import Any

        import httpx


        class UnexpectedStatus(Exception):
            \"\"\"Raised on an undocumented status when strict mode is enabled.\"\"\"

            def __init__(self, status_code: int, content: bytes):
                self.status_code = status_code
                self.content = content
                message = content.decode(errors=\"ignore\")
                super().__init__(
                    f\"Unexpected status code: {status_code}\\n\\nResponse content:\\n{message}\"
                )


        class NadeshikoError(Exception):
            \"\"\"Raised when the API returns a non-2xx problem response.\"\"\"

            def __init__(
                self,
                *,
                code: str,
                title: str,
                detail: str,
                status: int,
                type: str | None = None,
                trace_id: str | None = None,
                errors: Mapping[str, Any] | None = None,
                response: httpx.Response | None = None,
            ) -> None:
                super().__init__(detail or title or f\"API error {status}\")
                self.code = code
                self.title = title
                self.detail = detail
                self.status = status
                self.type = type
                self.trace_id = trace_id
                self.errors = dict(errors) if errors is not None else None
                self.response = response

            @classmethod
            def from_problem(
                cls,
                problem: Mapping[str, Any],
                *,
                response: httpx.Response | None = None,
            ) -> \"NadeshikoError\":
                status_value = problem.get(\"status\", response.status_code if response else 0)
                try:
                    status = int(status_value)
                except (TypeError, ValueError):
                    status = response.status_code if response else 0

                raw_errors = problem.get(\"errors\")
                errors: Mapping[str, Any] | None
                if isinstance(raw_errors, Mapping):
                    errors = raw_errors
                else:
                    errors = None

                trace_id = problem.get(\"instance\")
                if trace_id is not None:
                    trace_id = str(trace_id)

                type_value = problem.get(\"type\")
                if type_value is not None:
                    type_value = str(type_value)

                return cls(
                    code=str(problem.get(\"code\") or \"UNKNOWN_ERROR\"),
                    title=str(problem.get(\"title\") or \"Unexpected error\"),
                    detail=str(
                        problem.get(\"detail\")
                        or (response.text if response is not None else \"Unexpected API error\")
                    ),
                    status=status,
                    type=type_value,
                    trace_id=trace_id,
                    errors=errors,
                    response=response,
                )


        __all__ = [\"NadeshikoError\", \"UnexpectedStatus\"]
        """
    )


def _format_sdk_module(user_agent_name: str) -> str:
    return textwrap.dedent(
        f"""\
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

        T = TypeVar(\"T\")
        RETRYABLE_STATUS = {{408, 429, 500, 502, 503, 504}}
        ENVIRONMENTS = {{
            \"LOCAL\": \"http://localhost:5000/api\",
            \"DEVELOPMENT\": \"https://api-dev.nadeshiko.co\",
            \"PRODUCTION\": \"https://api.nadeshiko.co\",
        }}


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

                    wait_time = response.headers.get(\"Retry-After\")
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

                    wait_time = response.headers.get(\"Retry-After\")
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
            filtered = [arg for arg in get_args(annotation) if arg not in {{Unset, type(None)}}]
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
                        return {{k: convert_nested(vv) for k, vv in v.items()}}
                    if isinstance(v, (list, tuple)):
                        return [convert_nested(item) for item in v]
                    return v
                return body_type.from_dict({{k: convert_nested(v) for k, v in value.items()}})
            return value


        def _coerce_problem_value(value: Any) -> Any:
            if value is UNSET:
                return None
            if isinstance(value, Enum):
                return value.value
            if hasattr(value, \"to_dict\"):
                return value.to_dict()
            return value


        def _error_from_response(response: httpx.Response, parsed: Any) -> NadeshikoError:
            if parsed is not None and hasattr(parsed, \"code\") and hasattr(parsed, \"detail\"):
                problem = {{
                    \"code\": (
                        _coerce_problem_value(getattr(parsed, \"code\", None))
                        or \"UNKNOWN_ERROR\"
                    ),
                    \"title\": (
                        _coerce_problem_value(getattr(parsed, \"title\", None))
                        or \"Unexpected error\"
                    ),
                    \"detail\": _coerce_problem_value(getattr(parsed, \"detail\", None))
                    or response.text
                    or f\"HTTP {{response.status_code}}\",
                    \"status\": _coerce_problem_value(getattr(parsed, \"status\", None))
                    or response.status_code,
                    \"type\": _coerce_problem_value(
                        getattr(parsed, \"type_\", getattr(parsed, \"type\", None))
                    ),
                    \"instance\": _coerce_problem_value(getattr(parsed, \"instance\", None)),
                    \"errors\": _coerce_problem_value(getattr(parsed, \"errors\", None)),
                }}
                return NadeshikoError.from_problem(problem, response=response)

            try:
                payload = response.json()
            except ValueError:
                payload = None

            if isinstance(payload, Mapping):
                return NadeshikoError.from_problem(payload, response=response)

            return NadeshikoError(
                code=\"UNKNOWN_ERROR\",
                title=HTTPStatus(response.status_code).phrase,
                detail=response.text or f\"HTTP {{response.status_code}}\",
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
            _operation_cache: dict[str, _LoadedOperation] = {{}}

            def __init__(
                self,
                api_key: str,
                *,
                base_url: str = \"PRODUCTION\",
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
                base_headers = {{\"User-Agent\": f\"{user_agent_name}/{{__version__}}\"}}
                if headers:
                    base_headers.update(dict(headers))

                self.client = RawClient(
                    base_url=resolved_base_url,
                    token=api_key,
                    headers={{k: str(v) for k, v in base_headers.items()}},
                    timeout=resolved_timeout,
                    verify_ssl=verify_ssl,
                    follow_redirects=follow_redirects,
                    raise_on_unexpected_status=False,
                    httpx_args=dict(httpx_args or {{}}),
                )

                auth_value = (
                    f\"{{self.client.prefix}} {{self.client.token}}\"
                    if self.client.prefix
                    else self.client.token
                )
                auth_headers = {{self.client.auth_header_name: auth_value, **dict(base_headers)}}
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
                    if parameter.name not in path_params and parameter.name != \"body\"
                )
                body_parameter = signature.parameters.get(\"body\")
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
                path_values: dict[str, Any] = {{}}
                params = dict(kwargs)

                if operation.path_params:
                    if len(args) > len(operation.path_params):
                        raise TypeError(
                            f\"{{operation.metadata.name}}() accepts at most \"
                            f\"{{len(operation.path_params)}} positional arguments\"
                        )
                    for name, value in zip(operation.path_params, args):
                        annotation = operation.type_hints.get(name, inspect.Signature.empty)
                        path_values[name] = _coerce_annotation(value, annotation)
                    for name in operation.path_params[len(args):]:
                        if name not in params:
                            raise TypeError(f\"Missing required argument: '{{name}}'\")
                        annotation = operation.type_hints.get(name, inspect.Signature.empty)
                        path_values[name] = _coerce_annotation(params.pop(name), annotation)
                elif args:
                    if len(args) == 1 and hasattr(args[0], "to_dict"):
                        # Single model instance passed as positional arg - treat as body
                        params = {{"body": args[0], **params}}
                    else:
                        raise TypeError(
                            f\"{{operation.metadata.name}}() accepts keyword arguments only\"
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

                query_values: dict[str, Any] = {{}}
                for name in operation.query_params:
                    if name not in remaining:
                        continue
                    annotation = operation.type_hints.get(name, inspect.Signature.empty)
                    query_values[name] = _coerce_annotation(remaining.pop(name), annotation)
                request_kwargs.update(query_values)

                if operation.has_body:
                    body_hint = operation.type_hints.get(\"body\", inspect.Signature.empty)
                    if \"body\" in remaining:
                        body = _coerce_body(body_hint, remaining.pop(\"body\"))
                    elif remaining or operation.body_required:
                        body = _coerce_body(body_hint, remaining)
                        remaining = {{}}
                    else:
                        body = UNSET

                    if body is not UNSET:
                        request_kwargs[\"body\"] = body

                if remaining:
                    unexpected = ", ".join(sorted(remaining))
                    raise TypeError(
                        f\"Unexpected arguments for {{operation.metadata.name}}(): {{unexpected}}\"
                    )

                return request_kwargs

            def _extract_items(self, page: Any) -> list[Any]:
                attrs = getattr(type(page), \"__attrs_attrs__\", ())
                for attr in attrs:
                    value = getattr(page, attr.name)
                    if isinstance(value, list):
                        return value
                raise TypeError(
                    f\"{{type(page).__name__}} does not expose a paginated list field\"
                )

            def _pagination_cursor(self, page: Any) -> str | None:
                pagination = getattr(page, \"pagination\", None)
                if pagination is None:
                    return None
                has_more = getattr(
                    pagination, \"has_more\", getattr(pagination, \"hasMore\", False)
                )
                cursor = getattr(pagination, \"cursor\", None)
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
                if operation.has_body and \"body\" in updated:
                    body = updated[\"body\"]
                    if hasattr(body, \"to_dict\"):
                        body_payload = body.to_dict()
                    else:
                        body_payload = {{\"cursor\": cursor}}
                    body_payload[\"cursor\"] = cursor
                    updated[\"body\"] = body_payload
                else:
                    updated[\"cursor\"] = cursor
                return updated

            def close(self) -> None:
                self.client.get_httpx_client().close()

            async def aclose(self) -> None:
                await self.client.get_async_httpx_client().aclose()


        class Nadeshiko(_ClientBase):
            def __enter__(self) -> \"Nadeshiko\":
                self.client.get_httpx_client().__enter__()
                return self

            def __exit__(self, *args: Any, **kwargs: Any) -> None:
                self.client.get_httpx_client().__exit__(*args, **kwargs)

            def _request(self, operation_name: str, *args: Any, **kwargs: Any) -> Any:
                throw_on_error = kwargs.pop(\"throw_on_error\", True)
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
                    raise TypeError(f\"{{operation_name}} is not a paginated endpoint\")

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
            async def __aenter__(self) -> \"AsyncNadeshiko\":
                await self.client.get_async_httpx_client().__aenter__()
                return self

            async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
                await self.client.get_async_httpx_client().__aexit__(*args, **kwargs)

            async def _request(self, operation_name: str, *args: Any, **kwargs: Any) -> Any:
                throw_on_error = kwargs.pop(\"throw_on_error\", True)
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
                    raise TypeError(f\"{{operation_name}} is not a paginated endpoint\")

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
            method.__qualname__ = f\"Nadeshiko.{{name}}\"
            method.__doc__ = doc or f\"Call the {{name}} endpoint.\"
            return method


        def _make_sync_iterator(name: str, doc: str) -> Any:
            def method(self: Nadeshiko, *args: Any, **kwargs: Any) -> Iterator[Any]:
                return self._iterate(name, *args, **kwargs)

            method.__name__ = f\"iter_{{name}}\"
            method.__qualname__ = f\"Nadeshiko.iter_{{name}}\"
            method.__doc__ = doc or f\"Iterate through {{name}} results.\"
            return method


        def _make_async_method(name: str, doc: str) -> Any:
            async def method(self: AsyncNadeshiko, *args: Any, **kwargs: Any) -> Any:
                return await self._request(name, *args, **kwargs)

            method.__name__ = name
            method.__qualname__ = f\"AsyncNadeshiko.{{name}}\"
            method.__doc__ = doc or f\"Call the {{name}} endpoint asynchronously.\"
            return method


        def _make_async_iterator(name: str, doc: str) -> Any:
            async def method(self: AsyncNadeshiko, *args: Any, **kwargs: Any) -> AsyncIterator[Any]:
                async for item in self._iterate(name, *args, **kwargs):
                    yield item

            method.__name__ = f\"iter_{{name}}\"
            method.__qualname__ = f\"AsyncNadeshiko.iter_{{name}}\"
            method.__doc__ = doc or f\"Iterate through {{name}} results asynchronously.\"
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
                    f\"iter_{{_operation.name}}\",
                    _make_sync_iterator(_operation.name, _operation.doc),
                )
                setattr(
                    AsyncNadeshiko,
                    f\"iter_{{_operation.name}}\",
                    _make_async_iterator(_operation.name, _operation.doc),
                )


        __all__ = [
            \"AsyncNadeshiko\",
            \"Nadeshiko\",
            \"RawClient\",
            \"RetryOptions\",
            \"SDKResponse\",
        ]
        """
    )


def _format_stub_params(
    parameters: tuple[StubParameter, ...], *, include_throw_on_error: bool
) -> list[str]:
    parts: list[str] = []
    keyword_only_inserted = False

    for parameter in parameters:
        if parameter.keyword_only and not keyword_only_inserted:
            parts.append("*")
            keyword_only_inserted = True

        default = "" if parameter.required else " = ..."
        parts.append(f"{parameter.name}: {parameter.annotation}{default}")

    if include_throw_on_error:
        if not keyword_only_inserted:
            parts.append("*")
        parts.append("throw_on_error: Literal[True] = True")

    return parts


def _format_stub_method(
    operation: StubOperation,
    *,
    async_mode: bool,
    iterator: bool,
) -> list[str]:
    method_name = f"iter_{operation.name}" if iterator else operation.name
    prefix = "async def" if async_mode else "def"

    if iterator:
        return_type = operation.iterator_item_type or "Any"
        container = "AsyncIterator" if async_mode else "Iterator"
        params = [*operation.path_params, *operation.keyword_params]
        params_repr = ", ".join(_format_stub_params(tuple(params), include_throw_on_error=False))
        signature = f"    {prefix} {method_name}(self"
        if params_repr:
            signature += f", {params_repr}"
        signature += f") -> {container}[{return_type}]: ..."
        return [signature]

    params = [*operation.path_params, *operation.keyword_params]
    true_params = ", ".join(_format_stub_params(tuple(params), include_throw_on_error=True))
    false_params = ", ".join(
        _format_stub_params(tuple(params), include_throw_on_error=False)
        + ["throw_on_error: Literal[False]"]
    )
    return_type = operation.response_type

    true_sep = ", " if true_params else ""
    false_sep = ", " if false_params else ""
    overload_lines = [
        "    @overload",
        f"    {prefix} {method_name}(self{true_sep}{true_params}) -> {return_type}: ...",
        "    @overload",
        f"    {prefix} {method_name}(self{false_sep}{false_params})"
        f" -> SDKResponse[{return_type}]: ...",
    ]
    return overload_lines


def _format_sdk_stub(
    stub_operations: list[StubOperation],
    model_imports: set[str],
) -> str:
    model_imports_repr = ", ".join(sorted(model_imports))

    lines = [
        "from __future__ import annotations",
        "",
        "import datetime",
        "",
        "from collections.abc import AsyncIterator, Iterator, Mapping",
        "from typing import Any, Generic, Literal, TypeVar, overload",
        "",
        "import httpx",
        "",
        "from ._version import __version__",
        "from .client import AuthenticatedClient as RawClient",
        "from .errors import NadeshikoError",
    ]

    if model_imports_repr:
        lines.append(f"from .models import {model_imports_repr}")

    lines.extend(
        [
            "",
            'T = TypeVar("T")',
            "",
            "",
            "class RetryOptions:",
            "    max_retries: int",
            "    initial_delay: float",
            "    max_delay: float",
            "    timeout: float | httpx.Timeout | None",
            "",
            "    def __init__(",
            "        self,",
            "        max_retries: int = 2,",
            "        initial_delay: float = 0.5,",
            "        max_delay: float = 30.0,",
            "        timeout: float | httpx.Timeout | None = None,",
            "    ) -> None: ...",
            "",
            "",
            "class SDKResponse(Generic[T]):",
            "    response: httpx.Response",
            "    data: T | None",
            "    error: NadeshikoError | None",
            "",
            "    @property",
            "    def request(self) -> httpx.Request: ...",
            "",
            "",
            "class _ClientBase:",
            "    retry_options: RetryOptions",
            "    client: RawClient",
            "",
            "    def __init__(",
            "        self,",
            "        api_key: str,",
            '        *,',
            '        base_url: str = "PRODUCTION",',
            "        headers: Mapping[str, str] | None = None,",
            "        retry_options: RetryOptions | None = None,",
            "        timeout: float | httpx.Timeout | None = None,",
            "        verify_ssl: bool = True,",
            "        follow_redirects: bool = False,",
            "        httpx_args: Mapping[str, Any] | None = None,",
            "    ) -> None: ...",
            "",
            "    def close(self) -> None: ...",
            "    async def aclose(self) -> None: ...",
            "",
            "",
            "class Nadeshiko(_ClientBase):",
            '    def __enter__(self) -> "Nadeshiko": ...',
            "    def __exit__(self, *args: Any, **kwargs: Any) -> None: ...",
            "",
        ]
    )

    for operation in stub_operations:
        lines.extend(_format_stub_method(operation, async_mode=False, iterator=False))
        lines.append("")
        if operation.iterator_item_type is not None:
            lines.extend(_format_stub_method(operation, async_mode=False, iterator=True))
            lines.append("")

    lines.extend(
        [
            "",
            "class AsyncNadeshiko(_ClientBase):",
            '    async def __aenter__(self) -> "AsyncNadeshiko": ...',
            "    async def __aexit__(self, *args: Any, **kwargs: Any) -> None: ...",
            "",
        ]
    )

    for operation in stub_operations:
        lines.extend(_format_stub_method(operation, async_mode=True, iterator=False))
        lines.append("")
        if operation.iterator_item_type is not None:
            lines.extend(_format_stub_method(operation, async_mode=True, iterator=True))
            lines.append("")

    lines.extend(
        [
            "",
            '__all__ = ["AsyncNadeshiko", "Nadeshiko", "RawClient", "RetryOptions", "SDKResponse"]',
            "",
        ]
    )

    return "\n".join(lines)


def _format_init_module() -> str:
    return textwrap.dedent(
        """\
        \"\"\"A client library for accessing the Nadeshiko API.\"\"\"

        from ._version import __version__
        from .client import AuthenticatedClient as RawClient
        from .errors import NadeshikoError, UnexpectedStatus
        from .sdk import AsyncNadeshiko, Nadeshiko, RetryOptions, SDKResponse

        __all__ = (
            \"AsyncNadeshiko\",
            \"Nadeshiko\",
            \"NadeshikoError\",
            \"RawClient\",
            \"RetryOptions\",
            \"SDKResponse\",
            \"UnexpectedStatus\",
            \"__version__\",
        )
        """
    )


def write_wrapper_files(
    package_dir: Path,
    operations: list[WrapperOperation],
    *,
    user_agent_name: str,
) -> None:
    stub_operations, _input_types, stub_model_imports = collect_stub_data(
        package_dir,
        operations,
    )
    (package_dir / "_operations.py").write_text(
        _format_operations_module(operations),
        encoding="utf-8",
    )
    (package_dir / "errors.py").write_text(_format_errors_module(), encoding="utf-8")
    (package_dir / "sdk.py").write_text(
        _format_sdk_module(user_agent_name),
        encoding="utf-8",
    )
    (package_dir / "sdk.pyi").write_text(
        _format_sdk_stub(stub_operations, stub_model_imports),
        encoding="utf-8",
    )
    (package_dir / "inputs.py").unlink(missing_ok=True)
    (package_dir / "__init__.py").write_text(_format_init_module(), encoding="utf-8")
    (package_dir / "py.typed").write_text("", encoding="utf-8")
