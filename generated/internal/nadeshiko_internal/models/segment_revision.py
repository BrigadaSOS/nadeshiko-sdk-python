from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.segment_revision_snapshot import SegmentRevisionSnapshot


T = TypeVar("T", bound="SegmentRevision")


@_attrs_define
class SegmentRevision:
    """
    Attributes:
        id (int): Revision ID
        revision_number (int): Sequential revision number per segment
        snapshot (SegmentRevisionSnapshot): Snapshot of editable fields at the time of the revision
        created_at (datetime.datetime): When the revision was created
        user_name (None | str | Unset): Name of the user who made the change
    """

    id: int
    revision_number: int
    snapshot: SegmentRevisionSnapshot
    created_at: datetime.datetime
    user_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        revision_number = self.revision_number

        snapshot = self.snapshot.to_dict()

        created_at = self.created_at.isoformat()

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "revisionNumber": revision_number,
                "snapshot": snapshot,
                "createdAt": created_at,
            }
        )
        if user_name is not UNSET:
            field_dict["userName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment_revision_snapshot import SegmentRevisionSnapshot

        _src = dict(src_dict)
        id = _src.pop("id")

        revision_number = _src.pop("revisionNumber")

        snapshot = SegmentRevisionSnapshot.from_dict(_src.pop("snapshot"))

        created_at = datetime.datetime.fromisoformat(_src.pop("createdAt"))

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(_src.pop("userName", UNSET))

        segment_revision = cls(
            id=id,
            revision_number=revision_number,
            snapshot=snapshot,
            created_at=created_at,
            user_name=user_name,
        )

        segment_revision.additional_properties = _src
        return segment_revision

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
