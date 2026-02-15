from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.sentence import Sentence





T = TypeVar("T", bound="FetchSentenceContextResponse")



@_attrs_define
class FetchSentenceContextResponse:
    """ 
        Attributes:
            sentences (list[Sentence]):
     """

    sentences: list[Sentence]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sentence import Sentence
        sentences = []
        for sentences_item_data in self.sentences:
            sentences_item = sentences_item_data.to_dict()
            sentences.append(sentences_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sentences": sentences,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sentence import Sentence
        d = dict(src_dict)
        sentences = []
        _sentences = d.pop("sentences")
        for sentences_item_data in (_sentences):
            sentences_item = Sentence.from_dict(sentences_item_data)



            sentences.append(sentences_item)


        fetch_sentence_context_response = cls(
            sentences=sentences,
        )


        fetch_sentence_context_response.additional_properties = d
        return fetch_sentence_context_response

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
