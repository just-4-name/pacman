import pygame

from resources import GAME_OVER_IMG


class MenuWidgetsGetter:
    GAME_LOST_TEXT = 'Game Lost! Press space to restart'
    GAME_WON_TEXT = 'Game Won! Press space to restart'
    GAME_PAUSED_TEXT = 'Game Paused. Press space to restart'

    def __init__(self, block_size, block_cnt):
        self.__block_size = block_size
        self.__block_cnt = block_cnt

    def get_text_coords(self):
        return self.__block_cnt // 5 * self.__block_size, self.__block_cnt // 2 * self.__block_size

    def get_game_over_img(self):
        x_len = self.__block_cnt // 3 * 2 * self.__block_size
        return pygame.transform.scale(pygame.image.load(GAME_OVER_IMG), (x_len, x_len // 2))

    def get_img_coords(self):
        return self.__block_cnt // 6 * self.__block_size, self.__block_cnt // 6 * self.__block_size
