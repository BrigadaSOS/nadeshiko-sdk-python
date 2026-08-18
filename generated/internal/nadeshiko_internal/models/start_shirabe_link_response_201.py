from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StartShirabeLinkResponse201")


@_attrs_define
class StartShirabeLinkResponse201:
    """
    Attributes:
        authorize_url (str): Send the reader here. Shirabe asks them to approve, then redirects back.
        state (str): Opaque. Comes back on the redirect and must be handed to the callback unchanged.
    """

    authorize_url: str
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorize_url = self.authorize_url

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authorizeUrl": authorize_url,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        authorize_url = _src.pop("authorizeUrl")

        state = _src.pop("state")

        start_shirabe_link_response_201 = cls(
            authorize_url=authorize_url,
            state=state,
        )

        start_shirabe_link_response_201.additional_properties = _src
        return start_shirabe_link_response_201

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
