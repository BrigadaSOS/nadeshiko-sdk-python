from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_404_code import Error404Code, check_error_404_code
from ..models.error_404_status import Error404Status, check_error_404_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_404_errors import Error404Errors


T = TypeVar("T", bound="Error404")


@_attrs_define
class Error404:
    """Not Found error response

    Attributes:
        code (Error404Code): Specific error code for programmatic handling
        title (str): A short, human-readable summary of the problem
        detail (str): A human-readable explanation specific to this occurrence
        status (Error404Status): The HTTP status code
        type_ (str | Unset): A URI reference that identifies the problem type (e.g., GitHub issues link)
        instance (str | Unset): A URI reference that identifies the specific occurrence (e.g., trace ID)
        errors (Error404Errors | Unset): Optional map of field names to their error messages (for validation errors)
    """

    code: Error404Code
    title: str
    detail: str
    status: Error404Status
    type_: str | Unset = UNSET
    instance: str | Unset = UNSET
    errors: Error404Errors | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code: str = self.code

        title = self.title

        detail = self.detail

        status: int = self.status

        type_ = self.type_

        instance = self.instance

        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "title": title,
                "detail": detail,
                "status": status,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if instance is not UNSET:
            field_dict["instance"] = instance
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_404_errors import Error404Errors

        _src = dict(src_dict)
        code = check_error_404_code(_src.pop("code"))

        title = _src.pop("title")

        detail = _src.pop("detail")

        status = check_error_404_status(_src.pop("status"))

        type_ = _src.pop("type", UNSET)

        instance = _src.pop("instance", UNSET)

        _errors = _src.pop("errors", UNSET)
        errors: Error404Errors | Unset
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = Error404Errors.from_dict(_errors)

        error_404 = cls(
            code=code,
            title=title,
            detail=detail,
            status=status,
            type_=type_,
            instance=instance,
            errors=errors,
        )

        error_404.additional_properties = _src
        return error_404

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
