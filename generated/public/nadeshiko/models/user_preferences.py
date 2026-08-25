from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category import Category, check_category
from ..models.user_preferences_default_search_category import (
    UserPreferencesDefaultSearchCategory,
    check_user_preferences_default_search_category,
)
from ..models.user_preferences_media_card_default import (
    UserPreferencesMediaCardDefault,
    check_user_preferences_media_card_default,
)
from ..models.user_preferences_media_name_language import (
    UserPreferencesMediaNameLanguage,
    check_user_preferences_media_name_language,
)
from ..models.user_preferences_translation_languages_item import (
    UserPreferencesTranslationLanguagesItem,
    check_user_preferences_translation_languages_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_preferences_anki_profiles_item import UserPreferencesAnkiProfilesItem
    from ..models.user_preferences_content_rating_preferences import (
        UserPreferencesContentRatingPreferences,
    )
    from ..models.user_preferences_familiar_media import UserPreferencesFamiliarMedia
    from ..models.user_preferences_favorite_media_item import UserPreferencesFavoriteMediaItem
    from ..models.user_preferences_hidden_media_item import UserPreferencesHiddenMediaItem
    from ..models.user_preferences_product_emails import UserPreferencesProductEmails
    from ..models.user_preferences_search_history import UserPreferencesSearchHistory
    from ..models.user_preferences_translation_visibility_preferences import (
        UserPreferencesTranslationVisibilityPreferences,
    )
    from ..models.user_preferences_word_popup import UserPreferencesWordPopup


T = TypeVar("T", bound="UserPreferences")


@_attrs_define
class UserPreferences:
    """
    Attributes:
        media_name_language (UserPreferencesMediaNameLanguage | Unset): Preferred language for media names display
        content_rating_preferences (UserPreferencesContentRatingPreferences | Unset): Per-category content rating
            display preferences
        translation_visibility_preferences (UserPreferencesTranslationVisibilityPreferences | Unset): Per-language
            visibility mode for translations in search results, keyed by ISO 639-1 code (uppercase)
        translation_languages (list[UserPreferencesTranslationLanguagesItem] | Unset): Translation languages the reader
            wants in dictionary content, in display order. This is the global preference; translationVisibilityPreferences
            is a search-surface override for showing, spoiling, or hiding a language.
        word_popup (UserPreferencesWordPopup | Unset): How the word card behaves when a reader taps a word in a
            sentence. A group rather than a loose key so the settings that follow it have somewhere to live.
        search_history (UserPreferencesSearchHistory | Unset):
        anki_profiles (list[UserPreferencesAnkiProfilesItem] | Unset):
        default_search_category (UserPreferencesDefaultSearchCategory | Unset): Category tab a search opens on when the
            URL names none. `ALL` -- the value
            assumed when unset -- searches every category the user still has visible.

            Spelled out as its own enum rather than a nullable `Category` so that
            "search everything" is a value the client can send, not a field it has to
            clear. It mirrors `Category` plus `ALL`.

            A value the user has since hidden (see `hiddenCategories`) is ignored and
            the search falls back to `ALL`. It is stored rather than rejected, so
            unhiding the category brings the choice back.
        media_card_default (UserPreferencesMediaCardDefault | Unset): Whether the title card starts open or closed on a
            title's own page, and on
            a search narrowed to one title.

            The card is a disclosure: a single line -- thumbnail, title, sentence and
            episode counts -- with the alternate names, studio, season, airing status,
            genres and catalogue links folded underneath it. Anyone can open and close
            it from the card itself; this only decides which way it starts, and
            `OPEN` -- assumed when unset -- is that default.

            It exists because the card is context for a page whose subject is the
            sentence list underneath it. At its old fixed size on a phone it took
            roughly a third of the viewport, so every visit to a title a reader
            already knows began with the same scroll past the same card.
        hidden_categories (list[Category] | Unset): Whole media categories hidden from search results by the user.

            An empty array means nothing is hidden. Hiding *every* category is rejected with
            `400`: `filters.category` reads an empty list as "no filter", so hiding the last
            one would silently show everything back instead of nothing.
        hidden_media (list[UserPreferencesHiddenMediaItem] | Unset): Media hidden from search results by the user, as
            IDs.

            Entries used to carry the title's names as well. Nothing read them back --
            `GET /v1/user/excluded-media` resolves names from the catalogue, where a
            rename actually lands, and the search filter needs only IDs -- while the
            whole preferences blob rides `get-session` into the hydration payload of
            every page the reader loads. At ~141 bytes an entry against the 34 an
            ID-only one costs, a reader who had hidden 200 titles carried ~21KB of
            duplicated catalogue on every render.

            Still an object wrapping the ID rather than a bare string. Dropping the
            optional name fields is a change every previously-valid reader already
            accepts; replacing the object with a string is not, and old clients
            reaching for `mediaPublicId` would read the list as empty and show the
            reader results they had hidden.
        favorite_media (list[UserPreferencesFavoriteMediaItem] | Unset): Media the reader has starred. Starred titles
            sort to the top of the search
            media filter; they change the ORDER of that list, never its contents, so a
            starred title the current query does not match simply is not there.

            Capped at 100 entries, refused with `400` beyond that. The cap is not
            cosmetic: the whole preferences column is rewritten on every change (see
            `mutateUserPreferences`), so an unbounded list would make every unrelated
            preference write more expensive for the rest of the account's life.

            `favoritedAt` is declared here and written by the server, unlike
            `hiddenMedia`'s `hiddenAt` -- which the client invents and this schema has
            never described. It is the one thing about a starred title that the
            catalogue cannot answer, which is why it stayed when the names went -- for
            the same reason they went from `hiddenMedia`.
        familiar_media (UserPreferencesFamiliarMedia | Unset): Whether to keep a monthly tally of which titles the
            reader studies, used to
            sort those titles up the search media filter.

            Deliberately NOT `searchHistory`: that preference governs the activity log
            (queries, timestamps, per-row deletion), this one governs an aggregate
            count per title per month. A reader can reasonably want the tally without
            the diary, so the two are stored apart, cleared apart, and expire apart.
            Existing readers who had `searchHistory` off were seeded to `false` here.
        product_emails (UserPreferencesProductEmails | Unset): Whether we may send this account the lifecycle mail — the
            day-7 note, the
            feedback ask, the monthly recap. Absent means yes: these are service
            messages about the functionality the reader uses, so the default is on and
            the reader turns it off, here or from the link in any of them.

            Does NOT govern transactional mail. Sign-in links and address verification
            are the account working rather than news about it, and honouring this flag
            for them would let somebody lock themselves out by unsubscribing.
    """

    media_name_language: UserPreferencesMediaNameLanguage | Unset = UNSET
    content_rating_preferences: UserPreferencesContentRatingPreferences | Unset = UNSET
    translation_visibility_preferences: UserPreferencesTranslationVisibilityPreferences | Unset = (
        UNSET
    )
    translation_languages: list[UserPreferencesTranslationLanguagesItem] | Unset = UNSET
    word_popup: UserPreferencesWordPopup | Unset = UNSET
    search_history: UserPreferencesSearchHistory | Unset = UNSET
    anki_profiles: list[UserPreferencesAnkiProfilesItem] | Unset = UNSET
    default_search_category: UserPreferencesDefaultSearchCategory | Unset = UNSET
    media_card_default: UserPreferencesMediaCardDefault | Unset = UNSET
    hidden_categories: list[Category] | Unset = UNSET
    hidden_media: list[UserPreferencesHiddenMediaItem] | Unset = UNSET
    favorite_media: list[UserPreferencesFavoriteMediaItem] | Unset = UNSET
    familiar_media: UserPreferencesFamiliarMedia | Unset = UNSET
    product_emails: UserPreferencesProductEmails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_name_language: str | Unset = UNSET
        if not isinstance(self.media_name_language, Unset):
            media_name_language = self.media_name_language

        content_rating_preferences: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_rating_preferences, Unset):
            content_rating_preferences = self.content_rating_preferences.to_dict()

        translation_visibility_preferences: dict[str, Any] | Unset = UNSET
        if not isinstance(self.translation_visibility_preferences, Unset):
            translation_visibility_preferences = self.translation_visibility_preferences.to_dict()

        translation_languages: list[str] | Unset = UNSET
        if not isinstance(self.translation_languages, Unset):
            translation_languages = []
            for translation_languages_item_data in self.translation_languages:
                translation_languages_item: str = translation_languages_item_data
                translation_languages.append(translation_languages_item)

        word_popup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.word_popup, Unset):
            word_popup = self.word_popup.to_dict()

        search_history: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_history, Unset):
            search_history = self.search_history.to_dict()

        anki_profiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.anki_profiles, Unset):
            anki_profiles = []
            for anki_profiles_item_data in self.anki_profiles:
                anki_profiles_item = anki_profiles_item_data.to_dict()
                anki_profiles.append(anki_profiles_item)

        default_search_category: str | Unset = UNSET
        if not isinstance(self.default_search_category, Unset):
            default_search_category = self.default_search_category

        media_card_default: str | Unset = UNSET
        if not isinstance(self.media_card_default, Unset):
            media_card_default = self.media_card_default

        hidden_categories: list[str] | Unset = UNSET
        if not isinstance(self.hidden_categories, Unset):
            hidden_categories = []
            for hidden_categories_item_data in self.hidden_categories:
                hidden_categories_item: str = hidden_categories_item_data
                hidden_categories.append(hidden_categories_item)

        hidden_media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hidden_media, Unset):
            hidden_media = []
            for hidden_media_item_data in self.hidden_media:
                hidden_media_item = hidden_media_item_data.to_dict()
                hidden_media.append(hidden_media_item)

        favorite_media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.favorite_media, Unset):
            favorite_media = []
            for favorite_media_item_data in self.favorite_media:
                favorite_media_item = favorite_media_item_data.to_dict()
                favorite_media.append(favorite_media_item)

        familiar_media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.familiar_media, Unset):
            familiar_media = self.familiar_media.to_dict()

        product_emails: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_emails, Unset):
            product_emails = self.product_emails.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if media_name_language is not UNSET:
            field_dict["mediaNameLanguage"] = media_name_language
        if content_rating_preferences is not UNSET:
            field_dict["contentRatingPreferences"] = content_rating_preferences
        if translation_visibility_preferences is not UNSET:
            field_dict["translationVisibilityPreferences"] = translation_visibility_preferences
        if translation_languages is not UNSET:
            field_dict["translationLanguages"] = translation_languages
        if word_popup is not UNSET:
            field_dict["wordPopup"] = word_popup
        if search_history is not UNSET:
            field_dict["searchHistory"] = search_history
        if anki_profiles is not UNSET:
            field_dict["ankiProfiles"] = anki_profiles
        if default_search_category is not UNSET:
            field_dict["defaultSearchCategory"] = default_search_category
        if media_card_default is not UNSET:
            field_dict["mediaCardDefault"] = media_card_default
        if hidden_categories is not UNSET:
            field_dict["hiddenCategories"] = hidden_categories
        if hidden_media is not UNSET:
            field_dict["hiddenMedia"] = hidden_media
        if favorite_media is not UNSET:
            field_dict["favoriteMedia"] = favorite_media
        if familiar_media is not UNSET:
            field_dict["familiarMedia"] = familiar_media
        if product_emails is not UNSET:
            field_dict["productEmails"] = product_emails

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_preferences_anki_profiles_item import UserPreferencesAnkiProfilesItem
        from ..models.user_preferences_content_rating_preferences import (
            UserPreferencesContentRatingPreferences,
        )
        from ..models.user_preferences_familiar_media import UserPreferencesFamiliarMedia
        from ..models.user_preferences_favorite_media_item import UserPreferencesFavoriteMediaItem
        from ..models.user_preferences_hidden_media_item import UserPreferencesHiddenMediaItem
        from ..models.user_preferences_product_emails import UserPreferencesProductEmails
        from ..models.user_preferences_search_history import UserPreferencesSearchHistory
        from ..models.user_preferences_translation_visibility_preferences import (
            UserPreferencesTranslationVisibilityPreferences,
        )
        from ..models.user_preferences_word_popup import UserPreferencesWordPopup

        _src = dict(src_dict)
        _media_name_language = _src.pop("mediaNameLanguage", UNSET)
        media_name_language: UserPreferencesMediaNameLanguage | Unset
        if isinstance(_media_name_language, Unset):
            media_name_language = UNSET
        else:
            media_name_language = check_user_preferences_media_name_language(_media_name_language)

        _content_rating_preferences = _src.pop("contentRatingPreferences", UNSET)
        content_rating_preferences: UserPreferencesContentRatingPreferences | Unset
        if isinstance(_content_rating_preferences, Unset):
            content_rating_preferences = UNSET
        else:
            content_rating_preferences = UserPreferencesContentRatingPreferences.from_dict(
                _content_rating_preferences
            )

        _translation_visibility_preferences = _src.pop("translationVisibilityPreferences", UNSET)
        translation_visibility_preferences: UserPreferencesTranslationVisibilityPreferences | Unset
        if isinstance(_translation_visibility_preferences, Unset):
            translation_visibility_preferences = UNSET
        else:
            translation_visibility_preferences = (
                UserPreferencesTranslationVisibilityPreferences.from_dict(
                    _translation_visibility_preferences
                )
            )

        _translation_languages = _src.pop("translationLanguages", UNSET)
        translation_languages: list[UserPreferencesTranslationLanguagesItem] | Unset = UNSET
        if _translation_languages is not UNSET:
            translation_languages = []
            for translation_languages_item_data in _translation_languages:
                translation_languages_item = check_user_preferences_translation_languages_item(
                    translation_languages_item_data
                )

                translation_languages.append(translation_languages_item)

        _word_popup = _src.pop("wordPopup", UNSET)
        word_popup: UserPreferencesWordPopup | Unset
        if isinstance(_word_popup, Unset):
            word_popup = UNSET
        else:
            word_popup = UserPreferencesWordPopup.from_dict(_word_popup)

        _search_history = _src.pop("searchHistory", UNSET)
        search_history: UserPreferencesSearchHistory | Unset
        if isinstance(_search_history, Unset):
            search_history = UNSET
        else:
            search_history = UserPreferencesSearchHistory.from_dict(_search_history)

        _anki_profiles = _src.pop("ankiProfiles", UNSET)
        anki_profiles: list[UserPreferencesAnkiProfilesItem] | Unset = UNSET
        if _anki_profiles is not UNSET:
            anki_profiles = []
            for anki_profiles_item_data in _anki_profiles:
                anki_profiles_item = UserPreferencesAnkiProfilesItem.from_dict(
                    anki_profiles_item_data
                )

                anki_profiles.append(anki_profiles_item)

        _default_search_category = _src.pop("defaultSearchCategory", UNSET)
        default_search_category: UserPreferencesDefaultSearchCategory | Unset
        if isinstance(_default_search_category, Unset):
            default_search_category = UNSET
        else:
            default_search_category = check_user_preferences_default_search_category(
                _default_search_category
            )

        _media_card_default = _src.pop("mediaCardDefault", UNSET)
        media_card_default: UserPreferencesMediaCardDefault | Unset
        if isinstance(_media_card_default, Unset):
            media_card_default = UNSET
        else:
            media_card_default = check_user_preferences_media_card_default(_media_card_default)

        _hidden_categories = _src.pop("hiddenCategories", UNSET)
        hidden_categories: list[Category] | Unset = UNSET
        if _hidden_categories is not UNSET:
            hidden_categories = []
            for hidden_categories_item_data in _hidden_categories:
                hidden_categories_item = check_category(hidden_categories_item_data)

                hidden_categories.append(hidden_categories_item)

        _hidden_media = _src.pop("hiddenMedia", UNSET)
        hidden_media: list[UserPreferencesHiddenMediaItem] | Unset = UNSET
        if _hidden_media is not UNSET:
            hidden_media = []
            for hidden_media_item_data in _hidden_media:
                hidden_media_item = UserPreferencesHiddenMediaItem.from_dict(hidden_media_item_data)

                hidden_media.append(hidden_media_item)

        _favorite_media = _src.pop("favoriteMedia", UNSET)
        favorite_media: list[UserPreferencesFavoriteMediaItem] | Unset = UNSET
        if _favorite_media is not UNSET:
            favorite_media = []
            for favorite_media_item_data in _favorite_media:
                favorite_media_item = UserPreferencesFavoriteMediaItem.from_dict(
                    favorite_media_item_data
                )

                favorite_media.append(favorite_media_item)

        _familiar_media = _src.pop("familiarMedia", UNSET)
        familiar_media: UserPreferencesFamiliarMedia | Unset
        if isinstance(_familiar_media, Unset):
            familiar_media = UNSET
        else:
            familiar_media = UserPreferencesFamiliarMedia.from_dict(_familiar_media)

        _product_emails = _src.pop("productEmails", UNSET)
        product_emails: UserPreferencesProductEmails | Unset
        if isinstance(_product_emails, Unset):
            product_emails = UNSET
        else:
            product_emails = UserPreferencesProductEmails.from_dict(_product_emails)

        user_preferences = cls(
            media_name_language=media_name_language,
            content_rating_preferences=content_rating_preferences,
            translation_visibility_preferences=translation_visibility_preferences,
            translation_languages=translation_languages,
            word_popup=word_popup,
            search_history=search_history,
            anki_profiles=anki_profiles,
            default_search_category=default_search_category,
            media_card_default=media_card_default,
            hidden_categories=hidden_categories,
            hidden_media=hidden_media,
            favorite_media=favorite_media,
            familiar_media=familiar_media,
            product_emails=product_emails,
        )

        user_preferences.additional_properties = _src
        return user_preferences

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
