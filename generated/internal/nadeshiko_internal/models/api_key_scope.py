from typing import Literal

ApiKeyScope = Literal[
    "ADD_MEDIA",
    "CREATE_COLLECTIONS",
    "DELETE_COLLECTIONS",
    "READ_ACTIVITY",
    "READ_COLLECTIONS",
    "READ_MEDIA",
    "READ_PROFILE",
    "REMOVE_MEDIA",
    "UPDATE_COLLECTIONS",
    "UPDATE_MEDIA",
    "WRITE_ACTIVITY",
    "WRITE_PROFILE",
]

API_KEY_SCOPE_VALUES: set[ApiKeyScope] = {
    "ADD_MEDIA",
    "CREATE_COLLECTIONS",
    "DELETE_COLLECTIONS",
    "READ_ACTIVITY",
    "READ_COLLECTIONS",
    "READ_MEDIA",
    "READ_PROFILE",
    "REMOVE_MEDIA",
    "UPDATE_COLLECTIONS",
    "UPDATE_MEDIA",
    "WRITE_ACTIVITY",
    "WRITE_PROFILE",
}


def check_api_key_scope(value: str) -> ApiKeyScope:
    if value in API_KEY_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_KEY_SCOPE_VALUES!r}")
