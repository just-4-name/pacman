import pygame.draw
from Map import *
from pacman.Block import Block


class Pacman:
    Yellow = (255, 255, 0)

    def __init__(self, mapp):
        self.__x__ = 60
        self.__y__ = 60
        self.__speed_x__ = self.abs_speed = 1
        self.__speed_y__ = 0
        self.__map__ = mapp
        self.__radius__ = self.__map__.block_size / 2.25

    def update(self, dt):
        self.__x__ += self.__speed_x__ * dt
        self.__y__ += self.__speed_y__ * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.Yellow, (self.__x__, self.__y__), self.__radius__)

    def __is_valid__(self, block):
        return 0 <= block.row < len(self.__map__.blocks) and 0 <= block.col < len(self.__map__.blocks[0])

    def update_direction(self, event_key):
        cur_pos = Block(self.__x__, self.__y__, self.__map__.block_size)
        row = cur_pos.row
        col = cur_pos.col
        if event_key == pygame.K_w and row > 0 and self.__map__.blocks[row - 1][col] == BlockType.space:
            if self.__speed_y__ == 0:
                self.__x__ = self.__map__.block_size * (col + 0.5)
            self.__speed_y__ = -self.abs_speed
            self.__speed_x__ = 0
        elif event_key == pygame.K_s and row + 1 < len(self.__map__.blocks) and \
                self.__map__.blocks[row + 1][col] == BlockType.space:
            if self.__speed_y__ == 0:
                self.__x__ = self.__map__.block_size * (col + 0.5)
            self.__speed_y__ = self.abs_speed
            self.__speed_x__ = 0
        elif event_key == pygame.K_a and col > 0 and \
                self.__map__.blocks[row][col - 1] == BlockType.space:
            if self.__speed_x__ == 0:
                self.__y__ = self.__map__.block_size * (row + 0.5)
            self.__speed_x__ = -self.abs_speed
            self.__speed_y__ = 0
        elif event_key == pygame.K_d and col + 1 < len(self.__map__.blocks[0]) and \
                self.__map__.blocks[row][col + 1] == BlockType.space:
            if self.__speed_x__ == 0:
                self.__y__ = self.__map__.block_size * (row + 0.5)
            self.__speed_x__ = self.abs_speed
            self.__speed_y__ = 0

    def check_collision(self):
        blocks = [Block(self.__x__ - self.__radius__, self.__y__, self.__map__.block_size),
                  Block(self.__x__ + self.__radius__, self.__y__, self.__map__.block_size),
                  Block(self.__x__, self.__y__ - self.__radius__, self.__map__.block_size),
                  Block(self.__x__, self.__y__ + self.__radius__, self.__map__.block_size)]
        for block in blocks:
            if self.__is_valid__(block) and self.__map__.blocks[block.row][block.col] == BlockType.wall:
                self.__speed_x__ = self.__speed_y__ = 0
                return
