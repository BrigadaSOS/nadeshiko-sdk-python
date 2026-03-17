from enum import Enum


class GetSegmentByUuidIncludeItem(str, Enum):
    HASHEDID = "hashedId"
    POSANALYSIS = "posAnalysis"
    RATINGANALYSIS = "ratingAnalysis"
    STORAGE = "storage"
    STORAGEBASEPATH = "storageBasePath"

    def __str__(self) -> str:
        return str(self.value)
