from MapBuilder import *
from Pacman import Pacman


class World:
    __blocks_size__ = 40

    def __init__(self, screen):
        map_builder = MapBuilder(self.__blocks_size__)
        self.__map__ = map_builder.get_map()
        self.__pacman__ = Pacman(self.__map__)
        self.__screen__ = screen
        self.__ghosts__ = map_builder.get_ghosts()

    def update(self):
        self.__pacman__.update(1)
        self.__screen__.fill((0, 0, 0))
        for ghost in self.__ghosts__:
            ghost.update(1, Block(self.__pacman__.__x__, self.__pacman__.__y__, self.__blocks_size__))
        self.__check_collisions__()

    def draw(self):
        for ghost in self.__ghosts__:
            ghost.draw(self.__screen__)
        self.__map__.draw(self.__screen__)
        self.__pacman__.draw(self.__screen__)

    def update_direction(self, event_key):
        self.__pacman__.update_direction(event_key)

    def __check_collisions__(self):
        self.__pacman__.check_collision()
        # TODO pacman-ghost collision
