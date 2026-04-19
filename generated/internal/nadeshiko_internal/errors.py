"""Contains shared errors types that can be raised from API functions."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import httpx


class UnexpectedStatus(Exception):
    """Raised on an undocumented status when strict mode is enabled."""

    def __init__(self, status_code: int, content: bytes):
        self.status_code = status_code
        self.content = content
        message = content.decode(errors="ignore")
        super().__init__(
            f"Unexpected status code: {status_code}\n\nResponse content:\n{message}"
        )


class NadeshikoError(Exception):
    """Raised when the API returns a non-2xx problem response."""

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
        super().__init__(detail or title or f"API error {status}")
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
    ) -> "NadeshikoError":
        status_value = problem.get("status", response.status_code if response else 0)
        try:
            status = int(status_value)
        except (TypeError, ValueError):
            status = response.status_code if response else 0

        raw_errors = problem.get("errors")
        errors: Mapping[str, Any] | None
        if isinstance(raw_errors, Mapping):
            errors = raw_errors
        else:
            errors = None

        trace_id = problem.get("instance")
        if trace_id is not None:
            trace_id = str(trace_id)

        type_value = problem.get("type")
        if type_value is not None:
            type_value = str(type_value)

        return cls(
            code=str(problem.get("code") or "UNKNOWN_ERROR"),
            title=str(problem.get("title") or "Unexpected error"),
            detail=str(
                problem.get("detail")
                or (response.text if response is not None else "Unexpected API error")
            ),
            status=status,
            type=type_value,
            trace_id=trace_id,
            errors=errors,
            response=response,
        )


__all__ = ["NadeshikoError", "UnexpectedStatus"]
