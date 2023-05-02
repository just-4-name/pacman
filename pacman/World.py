import pygame
from utils.MapLoader import MapLoader
from objects.Map import Singleton


class World(metaclass=Singleton):
    BLOCK_SIZE = 40

    def __init__(self, screen):
        map_loader = MapLoader(self.BLOCK_SIZE)
        self.__map = map_loader.map
        self.__pacman = map_loader.pacman
        self.__screen = screen
        self.__ghosts = map_loader.ghosts

    def update(self):
        self.__pacman.update(1)
        self.__screen.fill((0, 0, 0))
        for ghost in self.__ghosts:
            ghost.update(1, self.__pacman.cur_block)
        return self.__check_collisions()

    def draw(self):
        for ghost in self.__ghosts:
            ghost.draw(self.__screen)
        self.__map.draw(self.__screen)
        self.__pacman.draw(self.__screen)

    def update_direction(self, event_key):
        pacman_moves = {pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d}
        if event_key in pacman_moves:
            self.__pacman.update_direction(event_key)

    def __check_collisions(self):
        self.__pacman.check_collision()
        for ghost in self.__ghosts:
            if ghost.check_collision(self.__pacman.circle):
                return True
        return False
