from typing import Literal

AdminUserWithProvidersRole = Literal["ADMIN", "MOD", "PATREON", "USER"]

ADMIN_USER_WITH_PROVIDERS_ROLE_VALUES: set[AdminUserWithProvidersRole] = {
    "ADMIN",
    "MOD",
    "PATREON",
    "USER",
}


def check_admin_user_with_providers_role(value: str) -> AdminUserWithProvidersRole:
    if value in ADMIN_USER_WITH_PROVIDERS_ROLE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADMIN_USER_WITH_PROVIDERS_ROLE_VALUES!r}"
    )
