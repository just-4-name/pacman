from utils.BlockType import BlockType
import pygame
from utils.Singleton import Singleton


class Map(metaclass=Singleton):
    BLUE = (0, 0, 255)

    def __init__(self, blocks, block_size):
        self.__block_size = block_size
        self.__blocks = blocks
        self.__EPS = self.__block_size / 10

    def draw(self, screen):
        for i in range(len(self.__blocks)):
            for j in range(len(self.__blocks[i])):
                if self.__blocks[i][j] == BlockType.WALL:
                    pygame.draw.rect(screen, self.BLUE, (j * self.__block_size, i * self.__block_size,
                                                         self.__block_size, self.__block_size))

    def picked_coin(self, block):
        self.blocks[block.y][block.x] = BlockType.SPACE

    @property
    def blocks(self):
        return self.__blocks

    @property
    def block_size(self):
        return self.__block_size

    @property
    def eps(self):
        return self.__EPS
