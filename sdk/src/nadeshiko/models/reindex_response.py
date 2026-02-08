from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.reindex_response_errors_item import ReindexResponseErrorsItem
  from ..models.reindex_response_stats import ReindexResponseStats





T = TypeVar("T", bound="ReindexResponse")



@_attrs_define
class ReindexResponse:
    """ Response from the reindex operation

        Attributes:
            success (bool | Unset): Whether the reindex operation completed successfully
            message (str | Unset): Human-readable message about the reindex operation
            stats (ReindexResponseStats | Unset): Statistics about the reindex operation
            errors (list[ReindexResponseErrorsItem] | Unset): Array of errors that occurred during reindexing (if any)
     """

    success: bool | Unset = UNSET
    message: str | Unset = UNSET
    stats: ReindexResponseStats | Unset = UNSET
    errors: list[ReindexResponseErrorsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reindex_response_errors_item import ReindexResponseErrorsItem
        from ..models.reindex_response_stats import ReindexResponseStats
        success = self.success

        message = self.message

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message
        if stats is not UNSET:
            field_dict["stats"] = stats
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reindex_response_errors_item import ReindexResponseErrorsItem
        from ..models.reindex_response_stats import ReindexResponseStats
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: ReindexResponseStats | Unset
        if isinstance(_stats,  Unset):
            stats = UNSET
        else:
            stats = ReindexResponseStats.from_dict(_stats)




        _errors = d.pop("errors", UNSET)
        errors: list[ReindexResponseErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ReindexResponseErrorsItem.from_dict(errors_item_data)



                errors.append(errors_item)


        reindex_response = cls(
            success=success,
            message=message,
            stats=stats,
            errors=errors,
        )


        reindex_response.additional_properties = d
        return reindex_response

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
