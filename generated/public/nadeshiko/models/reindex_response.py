from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reindex_response_errors_item import ReindexResponseErrorsItem
    from ..models.reindex_response_stats import ReindexResponseStats


T = TypeVar("T", bound="ReindexResponse")


@_attrs_define
class ReindexResponse:
    """Response from the reindex operation

    Attributes:
        success (bool): Whether the reindex operation completed successfully
        message (str): Human-readable message about the reindex operation
        stats (ReindexResponseStats): Statistics about the reindex operation
        errors (list[ReindexResponseErrorsItem]): Array of errors that occurred during reindexing (if any)
    """

    success: bool
    message: str
    stats: ReindexResponseStats
    errors: list[ReindexResponseErrorsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        stats = self.stats.to_dict()

        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "message": message,
                "stats": stats,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reindex_response_errors_item import ReindexResponseErrorsItem
        from ..models.reindex_response_stats import ReindexResponseStats

        _src = dict(src_dict)
        success = _src.pop("success")

        message = _src.pop("message")

        stats = ReindexResponseStats.from_dict(_src.pop("stats"))

        errors = []
        _errors = _src.pop("errors")
        for errors_item_data in _errors:
            errors_item = ReindexResponseErrorsItem.from_dict(errors_item_data)

            errors.append(errors_item)

        reindex_response = cls(
            success=success,
            message=message,
            stats=stats,
            errors=errors,
        )

        reindex_response.additional_properties = _src
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
