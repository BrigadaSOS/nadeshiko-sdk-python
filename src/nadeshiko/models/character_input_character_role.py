from enum import Enum


class CharacterInputCharacterRole(str, Enum):
    BACKGROUND = "BACKGROUND"
    MAIN = "MAIN"
    SUPPORTING = "SUPPORTING"

    def __str__(self) -> str:
        return str(self.value)
