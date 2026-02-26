from enum import Enum


class TrackUserActivityBodyActivityType(str, Enum):
    SEGMENT_PLAY = "SEGMENT_PLAY"

    def __str__(self) -> str:
        return str(self.value)
