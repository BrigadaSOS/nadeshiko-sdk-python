from enum import Enum


class SearchFiltersLanguagesItem(str, Enum):
    EN = "EN"
    ES = "ES"

    def __str__(self) -> str:
        return str(self.value)
