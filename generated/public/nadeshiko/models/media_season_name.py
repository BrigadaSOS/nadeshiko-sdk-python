from enum import Enum


class MediaSeasonName(str, Enum):
    FALL = "FALL"
    SPRING = "SPRING"
    SUMMER = "SUMMER"
    WINTER = "WINTER"

    def __str__(self) -> str:
        return str(self.value)
