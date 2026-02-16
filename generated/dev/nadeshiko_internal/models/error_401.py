from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_401_code import Error401Code
from ..models.error_401_status import Error401Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_401_errors import Error401Errors


T = TypeVar("T", bound="Error401")


@_attrs_define
class Error401:
    """Unauthorized error response

    Attributes:
        code (Error401Code): Specific error code for programmatic handling
        title (str): A short, human-readable summary of the problem
        detail (str): A human-readable explanation specific to this occurrence
        status (Error401Status): The HTTP status code
        type_ (str | Unset): A URI reference that identifies the problem type (e.g., GitHub issues link)
        instance (str | Unset): A URI reference that identifies the specific occurrence (e.g., trace ID)
        errors (Error401Errors | Unset): Optional map of field names to their error messages (for validation errors)
    """

    code: Error401Code
    title: str
    detail: str
    status: Error401Status
    type_: str | Unset = UNSET
    instance: str | Unset = UNSET
    errors: Error401Errors | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        title = self.title

        detail = self.detail

        status = self.status.value

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
        from ..models.error_401_errors import Error401Errors

        d = dict(src_dict)
        code = Error401Code(d.pop("code"))

        title = d.pop("title")

        detail = d.pop("detail")

        status = Error401Status(d.pop("status"))

        type_ = d.pop("type", UNSET)

        instance = d.pop("instance", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: Error401Errors | Unset
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = Error401Errors.from_dict(_errors)

        error_401 = cls(
            code=code,
            title=title,
            detail=detail,
            status=status,
            type_=type_,
            instance=instance,
            errors=errors,
        )

        error_401.additional_properties = d
        return error_401

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
