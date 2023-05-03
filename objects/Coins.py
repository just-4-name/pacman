import pygame
import enum

from objects.Map import BlockType
from utils.Singleton import Singleton


class PickedWhat(enum.Enum):
    NOTHING = 0
    COIN = 1
    KILLER_COIN = 2


class Coins(metaclass=Singleton):
    __WHITE = (255, 255, 255)
    __COIN_SIDE_TO_BLOCK_SZ_RATIO = 0.2
    __KILLER_COIN_SIDE_TO_BLOCK_SZ_RATIO = 0.6

    def __init__(self, mapp, initial_cnt_coins):
        self.__initial_cnt_coins = initial_cnt_coins
        self.__map = mapp

    def draw(self, screen):
        for i in range(len(self.__map.blocks)):
            for j in range(len(self.__map.blocks[0])):
                if self.__map.blocks[i][j] == BlockType.COIN:
                    indent = 0.5 - self.__COIN_SIDE_TO_BLOCK_SZ_RATIO / 2
                    side_len = self.__COIN_SIDE_TO_BLOCK_SZ_RATIO * self.__map.block_size
                    pygame.draw.rect(screen, self.__WHITE,
                                     ((j + indent) * self.__map.block_size, (i + indent) * self.__map.block_size,
                                      side_len, side_len))
                if self.__map.blocks[i][j] == BlockType.KILLER_COIN:
                    rad = self.__KILLER_COIN_SIDE_TO_BLOCK_SZ_RATIO * self.__map.block_size // 2
                    pygame.draw.circle(screen, self.__WHITE,
                                       ((j + 0.5) * self.__map.block_size, (i + 0.5) * self.__map.block_size), rad)

    def check_collision(self, block, dist_to_center):

        if self.__map.blocks[block.y][block.x] == BlockType.COIN and \
                dist_to_center < self.__map.block_size * self.__COIN_SIDE_TO_BLOCK_SZ_RATIO / 2:
            self.__map.picked_coin(block)
            return PickedWhat.COIN
        if self.__map.blocks[block.y][block.x] == BlockType.KILLER_COIN and \
                dist_to_center < self.__map.block_size * self.__KILLER_COIN_SIDE_TO_BLOCK_SZ_RATIO / 2:
            self.__map.picked_coin(block)
            return PickedWhat.KILLER_COIN
        return PickedWhat.NOTHING

    def check_if_won(self, score):
        return self.__initial_cnt_coins == score

    def restore_coins(self):
        self.__map.restore_coins()
