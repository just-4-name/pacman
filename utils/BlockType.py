import enum


class BlockType(enum.Enum):
    WALL = 0
    SPACE = 1
    COIN = 2
    KILLER_COIN = 3
    KILLER_COIN_PICKED = 4
