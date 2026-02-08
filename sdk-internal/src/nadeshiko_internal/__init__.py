
""" A client library for accessing Nadeshiko API """

from ._version import __version__
from .client import AuthenticatedClient as Nadeshiko

__all__ = (
    "Nadeshiko",
    "__version__",
)
