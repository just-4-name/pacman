import enum
import pygame


class BlockType(enum.Enum):
    wall = 1
    space = 0


class Map:
    BLUE = (0, 0, 255)

    def __init__(self, blocks, block_size):
        self.block_size = block_size
        self.blocks = blocks

    def draw(self, screen):
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                if self.blocks[i][j] == BlockType.wall:
                    pygame.draw.rect(screen, self.BLUE, (j * self.block_size, i * self.block_size,
                                                         self.block_size, self.block_size))
