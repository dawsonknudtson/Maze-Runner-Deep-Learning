from enum import IntEnum, auto

class Role(IntEnum):
    NONE = auto()
    ENEMY = auto()
    ENTRANCE = auto()
    EXIT = auto()
    EXTERIOR = auto()
    REWARD = auto()
    WALL = auto()