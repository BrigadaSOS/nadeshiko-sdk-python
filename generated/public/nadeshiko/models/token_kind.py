from typing import Literal

TokenKind = Literal["compound", "counter", "expression", "function", "inflected", "symbol", "word"]

TOKEN_KIND_VALUES: set[TokenKind] = {
    "compound",
    "counter",
    "expression",
    "function",
    "inflected",
    "symbol",
    "word",
}


def check_token_kind(value: str) -> TokenKind:
    if value in TOKEN_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TOKEN_KIND_VALUES!r}")
