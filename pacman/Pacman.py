import pygame.draw
from Map import *
from Block import Block
from Circle import Circle


class Pacman(metaclass=Singleton):
    Yellow = (255, 255, 0)

    def __init__(self, mapp):
        self.__x = 60
        self.__y = 60
        self.__speed_x = self.abs_speed__ = 2
        self.__speed_y = 0
        self.__map = mapp
        self.__radius = self.__map.block_size / 2.25

    def update(self, dt):
        self.__x += self.__speed_x * dt
        self.__y += self.__speed_y * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.Yellow, (self.__x, self.__y), self.__radius)

    def __is_valid(self, block):
        return 0 <= block.row < len(self.__map.blocks) and 0 <= block.col < len(self.__map.blocks[0])

    def update_direction(self, event_key):
        cur_pos = Block(self.__x, self.__y, self.__map.block_size)
        row = cur_pos.row
        col = cur_pos.col
        center_x = self.__map.block_size * (col + 0.5)
        center_y = self.__map.block_size * (row + 0.5)
        max_dist = self.__map.block_size / 2 - self.__radius + self.__map.eps
        if event_key == pygame.K_w and row > 0 and self.__map.blocks[row - 1][col] == BlockType.space:
            if self.__speed_y == 0:
                if abs(self.__x - center_x) <= max_dist:
                    self.__x = center_x
                else:
                    return
            self.__speed_y = -self.abs_speed__
            self.__speed_x = 0
        elif event_key == pygame.K_s and row + 1 < len(self.__map.blocks) and \
                self.__map.blocks[row + 1][col] == BlockType.space:
            if self.__speed_y == 0:
                if abs(self.__x - center_x) <= max_dist:
                    self.__x = center_x
                else:
                    return
            self.__speed_y = self.abs_speed__
            self.__speed_x = 0
        elif event_key == pygame.K_a and col > 0 and \
                self.__map.blocks[row][col - 1] == BlockType.space:
            if self.__speed_x == 0:
                if abs(self.__y - center_y) <= max_dist:
                    self.__y = center_y
                else:
                    return
            self.__speed_x = -self.abs_speed__
            self.__speed_y = 0
        elif event_key == pygame.K_d and col + 1 < len(self.__map.blocks[0]) and \
                self.__map.blocks[row][col + 1] == BlockType.space:
            if self.__speed_x == 0:
                if abs(self.__y - center_y) <= max_dist:
                    self.__y = center_y
                else:
                    return
            self.__speed_x = self.abs_speed__
            self.__speed_y = 0

    def check_collision(self):
        blocks = [Block(self.__x - self.__radius, self.__y, self.__map.block_size),
                  Block(self.__x + self.__radius, self.__y, self.__map.block_size),
                  Block(self.__x, self.__y - self.__radius, self.__map.block_size),
                  Block(self.__x, self.__y + self.__radius, self.__map.block_size)]
        for block in blocks:
            if self.__is_valid(block) and self.__map.blocks[block.row][block.col] == BlockType.wall:
                self.__speed_x = self.__speed_y = 0
                return

    @property
    def cur_block(self):
        return Block(self.__x, self.__y, self.__map.block_size)

    @property
    def circle(self):
        return Circle(self.__x, self.__y, self.__radius)
