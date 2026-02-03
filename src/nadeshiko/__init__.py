"""A client library for accessing Nadeshiko API"""

from ._version import __version__
from .client import Environment, Nadeshiko

__all__ = (
    "Nadeshiko",
    "Environment",
    "__version__",
)
