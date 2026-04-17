"""A client library for accessing the Nadeshiko API."""

from ._version import __version__
from .client import AuthenticatedClient as RawClient
from .errors import NadeshikoError, UnexpectedStatus
from .sdk import AsyncNadeshiko, Nadeshiko, RetryOptions, SDKResponse

__all__ = (
    "AsyncNadeshiko",
    "Nadeshiko",
    "NadeshikoError",
    "RawClient",
    "RetryOptions",
    "SDKResponse",
    "UnexpectedStatus",
    "__version__",
)
