from typing import Literal, cast

RunAdminMediaAuditCategory = Literal["ANIME", "JDRAMA"]

RUN_ADMIN_MEDIA_AUDIT_CATEGORY_VALUES: set[RunAdminMediaAuditCategory] = {
    "ANIME",
    "JDRAMA",
}


def check_run_admin_media_audit_category(value: str) -> RunAdminMediaAuditCategory:
    if value in RUN_ADMIN_MEDIA_AUDIT_CATEGORY_VALUES:
        return cast(RunAdminMediaAuditCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RUN_ADMIN_MEDIA_AUDIT_CATEGORY_VALUES!r}"
    )
