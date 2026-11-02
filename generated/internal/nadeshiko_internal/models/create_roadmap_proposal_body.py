from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRoadmapProposalBody")


@_attrs_define
class CreateRoadmapProposalBody:
    """
    Attributes:
        source_url (str):
        title (str | Unset):
        note (str | Unset):
        proposer_name (str | Unset): Optional name to show publicly if the proposal is approved.
    """

    source_url: str
    title: str | Unset = UNSET
    note: str | Unset = UNSET
    proposer_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_url = self.source_url

        title = self.title

        note = self.note

        proposer_name = self.proposer_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceUrl": source_url,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if note is not UNSET:
            field_dict["note"] = note
        if proposer_name is not UNSET:
            field_dict["proposerName"] = proposer_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        source_url = _src.pop("sourceUrl")

        title = _src.pop("title", UNSET)

        note = _src.pop("note", UNSET)

        proposer_name = _src.pop("proposerName", UNSET)

        create_roadmap_proposal_body = cls(
            source_url=source_url,
            title=title,
            note=note,
            proposer_name=proposer_name,
        )

        create_roadmap_proposal_body.additional_properties = _src
        return create_roadmap_proposal_body

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
