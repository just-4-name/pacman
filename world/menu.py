import pygame

from utils.Singleton import Singleton
from utils.menu_vidgets_info_getter import MenuWidgetsGetter


class Menu(metaclass=Singleton):
    __FONT_SIZE = 28

    def __init__(self, screen, blocks_size, cnt_blocks):
        self.__screen = screen
        self.__font = pygame.font.SysFont("HOBO", self.__FONT_SIZE)
        self.__widgets_getter = MenuWidgetsGetter(blocks_size, cnt_blocks)
        self.__game_over_img = self.__widgets_getter.get_game_over_img()

    def __draw_game_over(self):
        self.__screen.fill((0, 0, 0))
        self.__screen.blit(self.__game_over_img, self.__widgets_getter.get_img_coords())

    def game_lost(self):
        self.__draw_game_over()
        self.__screen.blit(self.__font.render(self.__widgets_getter.GAME_LOST_TEXT, True, 'yellow'),
                           self.__widgets_getter.get_text_coords())

    def game_won(self):
        self.__draw_game_over()
        self.__screen.blit(self.__font.render(self.__widgets_getter.GAME_WON_TEXT, True, 'yellow'),
                           self.__widgets_getter.get_text_coords())

    def game_paused(self):
        self.__screen.fill((0, 0, 0))
        self.__screen.blit(self.__font.render(self.__widgets_getter.GAME_PAUSED_TEXT, True, 'yellow'),
                           self.__widgets_getter.get_text_coords())
