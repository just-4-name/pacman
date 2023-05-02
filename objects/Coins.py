import pygame
from objects.Map import BlockType
from utils.Singleton import Singleton


class Coins(metaclass=Singleton):
    WHITE = (255, 255, 255)
    COIN_SIDE_TO_BLOCK_SZ_RATIO = 0.2

    def __init__(self, mapp):
        self.__map = mapp

    def draw(self, screen):
        for i in range(len(self.__map.blocks)):
            for j in range(len(self.__map.blocks[0])):
                if self.__map.blocks[i][j] == BlockType.COIN:
                    indent = 0.5 - self.COIN_SIDE_TO_BLOCK_SZ_RATIO / 2
                    side_len = self.COIN_SIDE_TO_BLOCK_SZ_RATIO * self.__map.block_size
                    pygame.draw.rect(screen, self.WHITE,
                                     ((j + indent) * self.__map.block_size, (i + indent) * self.__map.block_size,
                                      side_len, side_len))

    def check_collision(self, block, dist_to_center):

        if self.__map.blocks[block.y][block.x] == BlockType.COIN and \
                dist_to_center < self.__map.block_size * self.COIN_SIDE_TO_BLOCK_SZ_RATIO / 2:
            self.__map.picked_coin(block)
            return True
        return False
