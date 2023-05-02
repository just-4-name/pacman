from utils.Block import Block
from utils.Circle import Circle
from utils.PathFinder import ShortestPathFinder
import pygame


class Ghost:
    Red = (255, 0, 0)

    def __init__(self, mapp, block):
        self.__x = mapp.block_size * (block.x + 0.5)
        self.__y = mapp.block_size * (block.y + 0.5)
        self.__map = mapp
        self.__speed_x = self.__speed_y = 0
        self.__abs_speed = 1
        self.__radius = mapp.block_size / 2

    def update(self, dt, target):
        self.__update_direction(target)
        self.__x += self.__speed_x * dt
        self.__y += self.__speed_y * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.Red, (self.__x, self.__y), self.__radius)

    def __update_direction(self, target):
        path_finder = ShortestPathFinder(self.__map)
        dx, dy = path_finder.get_direction(self.get_cur_block(), target)
        center_x = self.__map.block_size * (self.get_cur_block().x + 0.5)
        center_y = self.__map.block_size * (self.get_cur_block().y + 0.5)
        self.__speed_x = self.__speed_y = 0
        if dy != 0:
            if abs(self.__x - center_x) > self.__map.eps:
                self.__speed_x = self.__abs_speed if center_x > self.__x else -self.__abs_speed
            else:
                self.__x = center_x
                self.__speed_y = dy * self.__abs_speed
        else:
            if abs(self.__y - center_y) > self.__map.eps:
                self.__speed_y = self.__abs_speed if center_y > self.__y else -self.__abs_speed
            else:
                self.__y = center_y
                self.__speed_x = dx * self.__abs_speed

    def check_collision(self, circle):
        return Circle(self.__x, self.__y, self.__radius).intersects(circle)

    def get_cur_block(self):
        return Block(self.__x, self.__y, self.__map.block_size)
