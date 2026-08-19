from typing import Literal

AccountQuotaStateQuotaSource = Literal["default", "legacy_column", "override", "tier"]

ACCOUNT_QUOTA_STATE_QUOTA_SOURCE_VALUES: set[AccountQuotaStateQuotaSource] = {
    "default",
    "legacy_column",
    "override",
    "tier",
}


def check_account_quota_state_quota_source(value: str) -> AccountQuotaStateQuotaSource:
    if value in ACCOUNT_QUOTA_STATE_QUOTA_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACCOUNT_QUOTA_STATE_QUOTA_SOURCE_VALUES!r}"
    )
