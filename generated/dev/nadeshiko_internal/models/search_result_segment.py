from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_result_segment_status import SearchResultSegmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.japanese_search_content import JapaneseSearchContent
    from ..models.morpheme import Morpheme
    from ..models.translation_search_content import TranslationSearchContent


T = TypeVar("T", bound="SearchResultSegment")


@_attrs_define
class SearchResultSegment:
    """Segment details in search results

    Attributes:
        status (SearchResultSegmentStatus): Segment status Example: ACTIVE.
        uuid (UUID): Unique identifier for the segment Example: 3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e.
        position (int): Position of the segment within the episode Example: 1133.
        start_time (str): Timestamp in H:MM:SS.ffffff format indicating when the segment starts Example: 0:33:27.255000.
        end_time (str): Timestamp in H:MM:SS.ffffff format indicating when the segment ends Example: 0:33:28.464000.
        episode_number (int): Episode number where the segment appears Example: 1.
        ja (JapaneseSearchContent): Japanese content in search results with optional highlight
        en (TranslationSearchContent): Translation content in search results with optional highlight
        es (TranslationSearchContent): Translation content in search results with optional highlight
        is_nsfw (bool): Whether the segment contains NSFW content
        morphemes (list[Morpheme] | None | Unset): Morphological analysis of the Japanese content
    """

    status: SearchResultSegmentStatus
    uuid: UUID
    position: int
    start_time: str
    end_time: str
    episode_number: int
    ja: JapaneseSearchContent
    en: TranslationSearchContent
    es: TranslationSearchContent
    is_nsfw: bool
    morphemes: list[Morpheme] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        uuid = str(self.uuid)

        position = self.position

        start_time = self.start_time

        end_time = self.end_time

        episode_number = self.episode_number

        ja = self.ja.to_dict()

        en = self.en.to_dict()

        es = self.es.to_dict()

        is_nsfw = self.is_nsfw

        morphemes: list[dict[str, Any]] | None | Unset
        if isinstance(self.morphemes, Unset):
            morphemes = UNSET
        elif isinstance(self.morphemes, list):
            morphemes = []
            for morphemes_type_0_item_data in self.morphemes:
                morphemes_type_0_item = morphemes_type_0_item_data.to_dict()
                morphemes.append(morphemes_type_0_item)

        else:
            morphemes = self.morphemes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "uuid": uuid,
                "position": position,
                "startTime": start_time,
                "endTime": end_time,
                "episodeNumber": episode_number,
                "ja": ja,
                "en": en,
                "es": es,
                "isNsfw": is_nsfw,
            }
        )
        if morphemes is not UNSET:
            field_dict["morphemes"] = morphemes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.japanese_search_content import JapaneseSearchContent
        from ..models.morpheme import Morpheme
        from ..models.translation_search_content import TranslationSearchContent

        d = dict(src_dict)
        status = SearchResultSegmentStatus(d.pop("status"))

        uuid = UUID(d.pop("uuid"))

        position = d.pop("position")

        start_time = d.pop("startTime")

        end_time = d.pop("endTime")

        episode_number = d.pop("episodeNumber")

        ja = JapaneseSearchContent.from_dict(d.pop("ja"))

        en = TranslationSearchContent.from_dict(d.pop("en"))

        es = TranslationSearchContent.from_dict(d.pop("es"))

        is_nsfw = d.pop("isNsfw")

        def _parse_morphemes(data: object) -> list[Morpheme] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                morphemes_type_0 = []
                _morphemes_type_0 = data
                for morphemes_type_0_item_data in _morphemes_type_0:
                    morphemes_type_0_item = Morpheme.from_dict(morphemes_type_0_item_data)

                    morphemes_type_0.append(morphemes_type_0_item)

                return morphemes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Morpheme] | None | Unset, data)

        morphemes = _parse_morphemes(d.pop("morphemes", UNSET))

        search_result_segment = cls(
            status=status,
            uuid=uuid,
            position=position,
            start_time=start_time,
            end_time=end_time,
            episode_number=episode_number,
            ja=ja,
            en=en,
            es=es,
            is_nsfw=is_nsfw,
            morphemes=morphemes,
        )

        search_result_segment.additional_properties = d
        return search_result_segment

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
