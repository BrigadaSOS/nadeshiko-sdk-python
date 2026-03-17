from enum import Enum


class TrackUserActivityBodyActivityType(str, Enum):
    SEARCH = "SEARCH"
    SEGMENT_PLAY = "SEGMENT_PLAY"
    SHARE = "SHARE"

    def __str__(self) -> str:
        return str(self.value)
