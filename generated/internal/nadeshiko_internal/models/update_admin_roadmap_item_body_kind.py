from typing import Literal

UpdateAdminRoadmapItemBodyKind = Literal["CONTENT", "FEATURE"]

UPDATE_ADMIN_ROADMAP_ITEM_BODY_KIND_VALUES: set[UpdateAdminRoadmapItemBodyKind] = {
    "CONTENT",
    "FEATURE",
}


def check_update_admin_roadmap_item_body_kind(value: str) -> UpdateAdminRoadmapItemBodyKind:
    if value in UPDATE_ADMIN_ROADMAP_ITEM_BODY_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ADMIN_ROADMAP_ITEM_BODY_KIND_VALUES!r}"
    )
