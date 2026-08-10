from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.agent_activity_response_entries_item_current import (
        AgentActivityResponseEntriesItemCurrent,
    )
    from ..models.agent_activity_response_entries_item_snapshot import (
        AgentActivityResponseEntriesItemSnapshot,
    )


T = TypeVar("T", bound="AgentActivityResponseEntriesItem")


@_attrs_define
class AgentActivityResponseEntriesItem:
    """
    Attributes:
        revision_id (int): Revision ID
        revision_number (int): The revision number to pass to the restore endpoint to undo this edit
        segment_public_id (str): Public ID of the segment that was changed
        media_public_id (str): Public ID of the media the segment belongs to
        episode_number (int): Episode the segment belongs to
        snapshot (AgentActivityResponseEntriesItemSnapshot): The segment's editable fields as they were before this edit
        current (AgentActivityResponseEntriesItemCurrent): The same fields as they are now. Paired with `snapshot` this
            is the
            diff, without the caller having to fetch the segment separately.
        report_id (int | None): The report this edit answered, when it answered one
        acted_by (None | str): Account the service credential belongs to
        created_at (datetime.datetime): When the edit was made
    """

    revision_id: int
    revision_number: int
    segment_public_id: str
    media_public_id: str
    episode_number: int
    snapshot: AgentActivityResponseEntriesItemSnapshot
    current: AgentActivityResponseEntriesItemCurrent
    report_id: int | None
    acted_by: None | str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revision_id = self.revision_id

        revision_number = self.revision_number

        segment_public_id = self.segment_public_id

        media_public_id = self.media_public_id

        episode_number = self.episode_number

        snapshot = self.snapshot.to_dict()

        current = self.current.to_dict()

        report_id: int | None
        report_id = self.report_id

        acted_by: None | str
        acted_by = self.acted_by

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revisionId": revision_id,
                "revisionNumber": revision_number,
                "segmentPublicId": segment_public_id,
                "mediaPublicId": media_public_id,
                "episodeNumber": episode_number,
                "snapshot": snapshot,
                "current": current,
                "reportId": report_id,
                "actedBy": acted_by,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_activity_response_entries_item_current import (
            AgentActivityResponseEntriesItemCurrent,
        )
        from ..models.agent_activity_response_entries_item_snapshot import (
            AgentActivityResponseEntriesItemSnapshot,
        )

        _src = dict(src_dict)
        revision_id = _src.pop("revisionId")

        revision_number = _src.pop("revisionNumber")

        segment_public_id = _src.pop("segmentPublicId")

        media_public_id = _src.pop("mediaPublicId")

        episode_number = _src.pop("episodeNumber")

        snapshot = AgentActivityResponseEntriesItemSnapshot.from_dict(_src.pop("snapshot"))

        current = AgentActivityResponseEntriesItemCurrent.from_dict(_src.pop("current"))

        def _parse_report_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        report_id = _parse_report_id(_src.pop("reportId"))

        def _parse_acted_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        acted_by = _parse_acted_by(_src.pop("actedBy"))

        created_at = datetime.datetime.fromisoformat(_src.pop("createdAt"))

        agent_activity_response_entries_item = cls(
            revision_id=revision_id,
            revision_number=revision_number,
            segment_public_id=segment_public_id,
            media_public_id=media_public_id,
            episode_number=episode_number,
            snapshot=snapshot,
            current=current,
            report_id=report_id,
            acted_by=acted_by,
            created_at=created_at,
        )

        agent_activity_response_entries_item.additional_properties = _src
        return agent_activity_response_entries_item

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
