from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_filter_item import MediaFilterItem


T = TypeVar("T", bound="SearchFiltersMedia")


@_attrs_define
class SearchFiltersMedia:
    """Media inclusion/exclusion filters

    Attributes:
        include (list[MediaFilterItem] | Unset): Include only segments from these media (with optional episode filter).
            A `mediaPublicId` that matches no media is rejected with `400`: dropping it would
            turn a deliberately narrow request into an unfiltered one.
        exclude (list[MediaFilterItem] | Unset): Exclude segments from these media (with optional episode filter).
            A `mediaPublicId` that matches no media is ignored, since excluding a media that
            does not exist excludes nothing.

            The ceiling is far above `include`'s because the two grow differently: `include`
            is a caller narrowing a request by hand, while `exclude` carries the reader's
            whole hidden-media list, which grows with use. At 100 a reader who had hidden
            more than that got a `400` on every search they made.
    """

    include: list[MediaFilterItem] | Unset = UNSET
    exclude: list[MediaFilterItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.include, Unset):
            include = []
            for include_item_data in self.include:
                include_item = include_item_data.to_dict()
                include.append(include_item)

        exclude: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exclude, Unset):
            exclude = []
            for exclude_item_data in self.exclude:
                exclude_item = exclude_item_data.to_dict()
                exclude.append(exclude_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include is not UNSET:
            field_dict["include"] = include
        if exclude is not UNSET:
            field_dict["exclude"] = exclude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_filter_item import MediaFilterItem

        _src = dict(src_dict)
        _include = _src.pop("include", UNSET)
        include: list[MediaFilterItem] | Unset = UNSET
        if _include is not UNSET:
            include = []
            for include_item_data in _include:
                include_item = MediaFilterItem.from_dict(include_item_data)

                include.append(include_item)

        _exclude = _src.pop("exclude", UNSET)
        exclude: list[MediaFilterItem] | Unset = UNSET
        if _exclude is not UNSET:
            exclude = []
            for exclude_item_data in _exclude:
                exclude_item = MediaFilterItem.from_dict(exclude_item_data)

                exclude.append(exclude_item)

        search_filters_media = cls(
            include=include,
            exclude=exclude,
        )

        search_filters_media.additional_properties = _src
        return search_filters_media

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
