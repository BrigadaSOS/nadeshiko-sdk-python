from enum import Enum


class SearchFiltersLanguagesExcludeItem(str, Enum):
    EN = "en"
    ES = "es"

    def __str__(self) -> str:
        return str(self.value)
