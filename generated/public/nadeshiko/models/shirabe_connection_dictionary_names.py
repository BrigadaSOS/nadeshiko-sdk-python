from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ShirabeConnectionDictionaryNames")


@_attrs_define
class ShirabeConnectionDictionaryNames:
    """What each dictionary above is CALLED, keyed by slug, as Shirabe names it. A reader's own uploads are filed under
    content hashes, so a client printing the stack without this prints a list of hashes. Empty for a link made before
    Shirabe published the names; fall back to the slug.

        Example:
            {'jmdict': 'JMdict', 'yomitan-c89af12122021a8a': '三省堂国語辞典'}

    """

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        shirabe_connection_dictionary_names = cls()

        shirabe_connection_dictionary_names.additional_properties = _src
        return shirabe_connection_dictionary_names

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
