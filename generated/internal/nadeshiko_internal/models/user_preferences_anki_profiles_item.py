from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_preferences_anki_profiles_item_fields_item import (
        UserPreferencesAnkiProfilesItemFieldsItem,
    )


T = TypeVar("T", bound="UserPreferencesAnkiProfilesItem")


@_attrs_define
class UserPreferencesAnkiProfilesItem:
    """
    Attributes:
        id (str):
        name (str):
        server_address (str):
        deck (None | str | Unset):
        model (None | str | Unset):
        fields (list[UserPreferencesAnkiProfilesItemFieldsItem] | Unset):
        key (None | str | Unset):
        open_browser_on_export (bool | Unset): Whether exporting a card brings Anki's card browser to the front.

            Absent means true, which is what it did before the setting existed.
            Undeclared until now: the settings page has offered the switch all
            along, but a profile saved with it off came back from the server
            without the field at all, so turning it off appeared to save and then
            did nothing.
    """

    id: str
    name: str
    server_address: str
    deck: None | str | Unset = UNSET
    model: None | str | Unset = UNSET
    fields: list[UserPreferencesAnkiProfilesItemFieldsItem] | Unset = UNSET
    key: None | str | Unset = UNSET
    open_browser_on_export: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        server_address = self.server_address

        deck: None | str | Unset
        if isinstance(self.deck, Unset):
            deck = UNSET
        else:
            deck = self.deck

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        open_browser_on_export = self.open_browser_on_export

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "serverAddress": server_address,
            }
        )
        if deck is not UNSET:
            field_dict["deck"] = deck
        if model is not UNSET:
            field_dict["model"] = model
        if fields is not UNSET:
            field_dict["fields"] = fields
        if key is not UNSET:
            field_dict["key"] = key
        if open_browser_on_export is not UNSET:
            field_dict["openBrowserOnExport"] = open_browser_on_export

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_preferences_anki_profiles_item_fields_item import (
            UserPreferencesAnkiProfilesItemFieldsItem,
        )

        _src = dict(src_dict)
        id = _src.pop("id")

        name = _src.pop("name")

        server_address = _src.pop("serverAddress")

        def _parse_deck(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deck = _parse_deck(_src.pop("deck", UNSET))

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(_src.pop("model", UNSET))

        _fields = _src.pop("fields", UNSET)
        fields: list[UserPreferencesAnkiProfilesItemFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = UserPreferencesAnkiProfilesItemFieldsItem.from_dict(fields_item_data)

                fields.append(fields_item)

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(_src.pop("key", UNSET))

        open_browser_on_export = _src.pop("openBrowserOnExport", UNSET)

        user_preferences_anki_profiles_item = cls(
            id=id,
            name=name,
            server_address=server_address,
            deck=deck,
            model=model,
            fields=fields,
            key=key,
            open_browser_on_export=open_browser_on_export,
        )

        user_preferences_anki_profiles_item.additional_properties = _src
        return user_preferences_anki_profiles_item

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
