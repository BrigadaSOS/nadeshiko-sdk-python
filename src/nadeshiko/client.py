import ssl
from enum import Enum
from typing import Any

import httpx
from attrs import define, evolve, field


class Environment(Enum):
    """API environment presets."""

    LOCAL = "http://localhost:5000"
    PRODUCTION = "https://api.nadeshiko.co"


def _resolve_base_url(base_url: str | Environment) -> str:
    """Resolve environment enum to URL, or return URL string as-is."""
    if isinstance(base_url, Environment):
        return base_url.value
    return base_url


@define
class Nadeshiko:
    """Nadeshiko API client.

    Example:
        >>> from nadeshiko import Nadeshiko, Environment
        >>> from nadeshiko.api.search import search
        >>>
        >>> client = Nadeshiko(api_key="your-key")
        >>> result = search.sync(client=client, body={"query": "..."})

    Args:
        api_key: Your Nadeshiko API key
        base_url: API environment (Environment.PRODUCTION, Environment.LOCAL) or custom URL string
        timeout: Request timeout
        verify_ssl: Whether to verify SSL certificates
        follow_redirects: Whether to follow redirects
        raise_on_unexpected_status: Whether to raise on unexpected status codes
        httpx_args: Additional arguments for httpx.Client
    """

    _api_key: str = field(alias="api_key")
    _base_url: str | Environment = field(default=Environment.PRODUCTION, alias="base_url")
    _cookies: dict[str, str] = field(factory=dict, kw_only=True, alias="cookies")
    _headers: dict[str, str] = field(factory=dict, kw_only=True, alias="headers")
    _timeout: httpx.Timeout | None = field(default=None, kw_only=True, alias="timeout")
    _verify_ssl: str | bool | ssl.SSLContext = field(default=True, kw_only=True, alias="verify_ssl")
    _follow_redirects: bool = field(default=False, kw_only=True, alias="follow_redirects")
    _httpx_args: dict[str, Any] = field(factory=dict, kw_only=True, alias="httpx_args")
    _raise_on_unexpected_status: bool = field(
        default=False, kw_only=True, alias="raise_on_unexpected_status"
    )
    _client: httpx.Client | None = field(default=None, init=False)
    _async_client: httpx.AsyncClient | None = field(default=None, init=False)

    @property
    def raise_on_unexpected_status(self) -> bool:
        """Whether to raise on unexpected status codes."""
        return self._raise_on_unexpected_status

    def with_headers(self, headers: dict[str, str]) -> "Nadeshiko":
        """Get a new client matching this one with additional headers."""
        if self._client is not None:
            self._client.headers.update(headers)
        if self._async_client is not None:
            self._async_client.headers.update(headers)
        return evolve(self, headers={**self._headers, **headers})

    def with_cookies(self, cookies: dict[str, str]) -> "Nadeshiko":
        """Get a new client matching this one with additional cookies."""
        if self._client is not None:
            self._client.cookies.update(cookies)
        if self._async_client is not None:
            self._async_client.cookies.update(cookies)
        return evolve(self, cookies={**self._cookies, **cookies})

    def with_timeout(self, timeout: httpx.Timeout) -> "Nadeshiko":
        """Get a new client matching this one with a new timeout configuration."""
        if self._client is not None:
            self._client.timeout = timeout
        if self._async_client is not None:
            self._async_client.timeout = timeout
        return evolve(self, timeout=timeout)

    # Internal methods required by generated API functions
    # These are not part of the public API

    def set_httpx_client(self, client: httpx.Client) -> "Nadeshiko":
        self._client = client
        return self

    def get_httpx_client(self) -> httpx.Client:
        if self._client is None:
            headers = {**self._headers, "X-API-Key": self._api_key}
            self._client = httpx.Client(
                base_url=_resolve_base_url(self._base_url),
                cookies=self._cookies,
                headers=headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._client

    def __enter__(self) -> "Nadeshiko":
        self.get_httpx_client().__enter__()
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        self.get_httpx_client().__exit__(*args, **kwargs)

    def set_async_httpx_client(self, async_client: httpx.AsyncClient) -> "Nadeshiko":
        self._async_client = async_client
        return self

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        if self._async_client is None:
            headers = {**self._headers, "X-API-Key": self._api_key}
            self._async_client = httpx.AsyncClient(
                base_url=_resolve_base_url(self._base_url),
                cookies=self._cookies,
                headers=headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._async_client

    async def __aenter__(self) -> "Nadeshiko":
        await self.get_async_httpx_client().__aenter__()
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        await self.get_async_httpx_client().__aexit__(*args, **kwargs)
