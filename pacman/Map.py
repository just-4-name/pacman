import enum
import pygame


class BlockType(enum.Enum):
    wall = 1
    space = 0


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Map(metaclass=Singleton):
    BLUE = (0, 0, 255)

    def __init__(self, blocks, block_size):
        self.__block_size = block_size
        self.__blocks = blocks
        self.__EPS = self.__block_size / 10

    def draw(self, screen):
        for i in range(len(self.__blocks)):
            for j in range(len(self.__blocks[i])):
                if self.__blocks[i][j] == BlockType.wall:
                    pygame.draw.rect(screen, self.BLUE, (j * self.__block_size, i * self.__block_size,
                                                         self.__block_size, self.__block_size))

    @property
    def blocks(self):
        return self.__blocks

    @property
    def block_size(self):
        return self.__block_size

    @property
    def eps(self):
        return self.__EPS
