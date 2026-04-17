from enum import Enum


class MediaUpdateRequestSeasonName(str, Enum):
    FALL = "FALL"
    SPRING = "SPRING"
    SUMMER = "SUMMER"
    WINTER = "WINTER"

    def __str__(self) -> str:
        return str(self.value)
