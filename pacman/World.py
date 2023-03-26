from MapBuilder import *
from Pacman import Pacman


class World(metaclass=Singleton):
    BLOCK_SIZE = 40

    def __init__(self, screen):
        map_builder = MapBuilder(self.BLOCK_SIZE)
        self.__map = map_builder.map
        self.__pacman = Pacman(self.__map)
        self.__screen = screen
        self.__ghosts = map_builder.ghosts

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
        self.__pacman.update_direction(event_key)

    def __check_collisions(self):
        self.__pacman.check_collision()
        for ghost in self.__ghosts:
            if ghost.check_collision(self.__pacman.circle):
                return True
        return False
