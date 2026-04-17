from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.token import Token


T = TypeVar("T", bound="SegmentTextJa")


@_attrs_define
class SegmentTextJa:
    """
    Attributes:
        content (str): Original Japanese content Example: 僕は僕で、君は君だ。.
        highlight (None | str): Japanese `content` with `<mark>` tags wrapping terms that matched a search query. Only
            populated on segments returned from a search endpoint.
        tokens (list[Token] | None): Morphological tokens for interactive display. Populated only for segments with
            available POS analysis.
    """

    content: str
    highlight: None | str
    tokens: list[Token] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        highlight: None | str
        highlight = self.highlight

        tokens: list[dict[str, Any]] | None
        if isinstance(self.tokens, list):
            tokens = []
            for tokens_type_0_item_data in self.tokens:
                tokens_type_0_item = tokens_type_0_item_data.to_dict()
                tokens.append(tokens_type_0_item)

        else:
            tokens = self.tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "highlight": highlight,
                "tokens": tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token import Token

        _src = dict(src_dict)
        content = _src.pop("content")

        def _parse_highlight(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        highlight = _parse_highlight(_src.pop("highlight"))

        def _parse_tokens(data: object) -> list[Token] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tokens_type_0 = []
                _tokens_type_0 = data
                for tokens_type_0_item_data in _tokens_type_0:
                    tokens_type_0_item = Token.from_dict(tokens_type_0_item_data)

                    tokens_type_0.append(tokens_type_0_item)

                return tokens_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Token] | None, data)

        tokens = _parse_tokens(_src.pop("tokens"))

        segment_text_ja = cls(
            content=content,
            highlight=highlight,
            tokens=tokens,
        )

        segment_text_ja.additional_properties = _src
        return segment_text_ja

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
