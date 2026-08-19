from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shirabe_connection_dictionary_names import ShirabeConnectionDictionaryNames


T = TypeVar("T", bound="ShirabeConnection")


@_attrs_define
class ShirabeConnection:
    """A reader's linked Shirabe account, as the reader is shown it.

    Never carries the stored tokens: nothing here can be used to act on their
    Shirabe account.

        Attributes:
            needs_upgrade (bool): True when the link works but is missing a permission a newer feature needs -- granted
                before that feature existed. A re-consent, not a repair: what the account was linked for keeps working the whole
                time, and only the newer feature is unavailable.
            missing_scopes (list[str]): The permissions a re-consent would add. Empty unless `needsUpgrade`.
            disconnected (bool): True when Shirabe refused this key outright -- the reader revoked it from their Shirabe
                access list, or it was swept for being idle. The link is over until they make a new one, and their own
                dictionaries are not being used until they do. Distinct from `needsUpgrade`, which is a link that still works:
                this one is a repair.
            linked_at (datetime.datetime):
            scopes (list[str]): What the reader granted. Today that is READ_ACCOUNT and nothing else. Example:
                ['READ_ACCOUNT'].
            dictionaries (list[str]): Their Shirabe dictionary stack: ordered `slug:lang` refs naming which dictionaries
                resolve, in which languages, in what order. This is what makes a word lookup here answer the way it does over
                there. Example: ['sanseido:ja', 'jmdict:en'].
            stack_is_private (bool): True when their stack names one of their own uploads, which makes its answers theirs
                alone and stops a lookup being cached for anyone else.
            shirabe_name (None | str | Unset): Who they are on Shirabe, for the settings page to name the link. Example:
                Lumi.
            dictionary_names (ShirabeConnectionDictionaryNames | Unset): What each dictionary above is CALLED, keyed by
                slug, as Shirabe names it. A reader's own uploads are filed under content hashes, so a client printing the stack
                without this prints a list of hashes. Empty for a link made before Shirabe published the names; fall back to the
                slug. Example: {'jmdict': 'JMdict', 'yomitan-c89af12122021a8a': '三省堂国語辞典'}.
            synced_at (datetime.datetime | None | Unset): When the stack was last re-read from Shirabe.
    """

    needs_upgrade: bool
    missing_scopes: list[str]
    disconnected: bool
    linked_at: datetime.datetime
    scopes: list[str]
    dictionaries: list[str]
    stack_is_private: bool
    shirabe_name: None | str | Unset = UNSET
    dictionary_names: ShirabeConnectionDictionaryNames | Unset = UNSET
    synced_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        needs_upgrade = self.needs_upgrade

        missing_scopes = self.missing_scopes

        disconnected = self.disconnected

        linked_at = self.linked_at.isoformat()

        scopes = self.scopes

        dictionaries = self.dictionaries

        stack_is_private = self.stack_is_private

        shirabe_name: None | str | Unset
        if isinstance(self.shirabe_name, Unset):
            shirabe_name = UNSET
        else:
            shirabe_name = self.shirabe_name

        dictionary_names: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dictionary_names, Unset):
            dictionary_names = self.dictionary_names.to_dict()

        synced_at: None | str | Unset
        if isinstance(self.synced_at, Unset):
            synced_at = UNSET
        elif isinstance(self.synced_at, datetime.datetime):
            synced_at = self.synced_at.isoformat()
        else:
            synced_at = self.synced_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "needsUpgrade": needs_upgrade,
                "missingScopes": missing_scopes,
                "disconnected": disconnected,
                "linkedAt": linked_at,
                "scopes": scopes,
                "dictionaries": dictionaries,
                "stackIsPrivate": stack_is_private,
            }
        )
        if shirabe_name is not UNSET:
            field_dict["shirabeName"] = shirabe_name
        if dictionary_names is not UNSET:
            field_dict["dictionaryNames"] = dictionary_names
        if synced_at is not UNSET:
            field_dict["syncedAt"] = synced_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shirabe_connection_dictionary_names import ShirabeConnectionDictionaryNames

        _src = dict(src_dict)
        needs_upgrade = _src.pop("needsUpgrade")

        missing_scopes = cast(list[str], _src.pop("missingScopes"))

        disconnected = _src.pop("disconnected")

        linked_at = datetime.datetime.fromisoformat(_src.pop("linkedAt"))

        scopes = cast(list[str], _src.pop("scopes"))

        dictionaries = cast(list[str], _src.pop("dictionaries"))

        stack_is_private = _src.pop("stackIsPrivate")

        def _parse_shirabe_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shirabe_name = _parse_shirabe_name(_src.pop("shirabeName", UNSET))

        _dictionary_names = _src.pop("dictionaryNames", UNSET)
        dictionary_names: ShirabeConnectionDictionaryNames | Unset
        if isinstance(_dictionary_names, Unset):
            dictionary_names = UNSET
        else:
            dictionary_names = ShirabeConnectionDictionaryNames.from_dict(_dictionary_names)

        def _parse_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                synced_at_type_0 = datetime.datetime.fromisoformat(data)

                return synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        synced_at = _parse_synced_at(_src.pop("syncedAt", UNSET))

        shirabe_connection = cls(
            needs_upgrade=needs_upgrade,
            missing_scopes=missing_scopes,
            disconnected=disconnected,
            linked_at=linked_at,
            scopes=scopes,
            dictionaries=dictionaries,
            stack_is_private=stack_is_private,
            shirabe_name=shirabe_name,
            dictionary_names=dictionary_names,
            synced_at=synced_at,
        )

        shirabe_connection.additional_properties = _src
        return shirabe_connection

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
