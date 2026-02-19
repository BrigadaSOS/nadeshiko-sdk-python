from enum import Enum


class ReportTargetEpisodeType(str, Enum):
    EPISODE = "EPISODE"

    def __str__(self) -> str:
        return str(self.value)
