from enum import Enum


class MediaCreateRequestSeasonName(str, Enum):
    FALL = "FALL"
    SPRING = "SPRING"
    SUMMER = "SUMMER"
    WINTER = "WINTER"

    def __str__(self) -> str:
        return str(self.value)
