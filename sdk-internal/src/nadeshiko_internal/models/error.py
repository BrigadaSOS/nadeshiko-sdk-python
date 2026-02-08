from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.error_errors import ErrorErrors





T = TypeVar("T", bound="Error")



@_attrs_define
class Error:
    """ Error Response schema for all cases

        Attributes:
            code (str): Specific error code for programmatic handling
            title (str): A short, human-readable summary of the problem
            detail (str): A human-readable explanation specific to this occurrence
            status (int): The HTTP status code
            type_ (str | Unset): A URI reference that identifies the problem type (e.g., GitHub issues link)
            instance (str | Unset): A URI reference that identifies the specific occurrence (e.g., trace ID)
            errors (ErrorErrors | Unset): Optional map of field names to their error messages (for validation errors)
     """

    code: str
    title: str
    detail: str
    status: int
    type_: str | Unset = UNSET
    instance: str | Unset = UNSET
    errors: ErrorErrors | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.error_errors import ErrorErrors
        code = self.code

        title = self.title

        detail = self.detail

        status = self.status

        type_ = self.type_

        instance = self.instance

        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "title": title,
            "detail": detail,
            "status": status,
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if instance is not UNSET:
            field_dict["instance"] = instance
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_errors import ErrorErrors
        d = dict(src_dict)
        code = d.pop("code")

        title = d.pop("title")

        detail = d.pop("detail")

        status = d.pop("status")

        type_ = d.pop("type", UNSET)

        instance = d.pop("instance", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: ErrorErrors | Unset
        if isinstance(_errors,  Unset):
            errors = UNSET
        else:
            errors = ErrorErrors.from_dict(_errors)




        error = cls(
            code=code,
            title=title,
            detail=detail,
            status=status,
            type_=type_,
            instance=instance,
            errors=errors,
        )


        error.additional_properties = d
        return error

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
