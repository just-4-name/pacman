import pygame.draw
from utils.Block import Block
from objects.Map import BlockType, Singleton
from utils.Circle import Circle


class Pacman(metaclass=Singleton):
    Yellow = (255, 255, 0)

    def __init__(self, mapp, block):
        self.__x = mapp.block_size * (block.x + 0.5)
        self.__y = mapp.block_size * (block.y + 0.5)
        self.__intended_speed_x = self.__speed_x = self.abs_speed__ = 2
        self.__intended_speed_y = self.__speed_y = 0
        self.__map = mapp
        self.__radius = self.__map.block_size / 2 - self.__map.eps / 3

    def update(self, dt):
        if self.__speed_x != self.__intended_speed_x or self.__speed_y != self.__intended_speed_y:
            if self.__try_turn():
                self.__speed_y = self.__intended_speed_y
                self.__speed_x = self.__intended_speed_x
        self.__x += self.__speed_x * dt
        self.__y += self.__speed_y * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.Yellow, (self.__x, self.__y), self.__radius)
        pygame.draw.circle(screen, self.Yellow, (self.__x + self.__x_direction() * self.__map.block_size,
                                                 self.__y + self.__y_direction() * self.__map.block_size), self.__map.eps)

    def update_direction(self, event_key):
        self.__intended_speed_x = self.__intended_speed_y = 0
        if event_key == pygame.K_w:
            self.__intended_speed_y = -self.abs_speed__
        elif event_key == pygame.K_s:
            self.__intended_speed_y = self.abs_speed__
        elif event_key == pygame.K_a:
            self.__intended_speed_x = -self.abs_speed__
        elif event_key == pygame.K_d:
            self.__intended_speed_x = self.abs_speed__

    def check_collision(self):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy != 0 and dx != 0:
                    continue
                block = Block(self.__x + dx * self.__radius, self.__y + dy * self.__radius, self.__map.block_size)
                if self.__map.blocks[block.y][block.x] == BlockType.WALL:
                    self.__speed_x = self.__speed_y = 0

    def __try_turn(self):
        row = self.cur_block.y
        col = self.cur_block.x
        center_x = (col + 0.5) * self.__map.block_size
        center_y = (row + 0.5) * self.__map.block_size
        if self.__intended_speed_x == 0:
            if self.__speed_y != 0:
                return True
            elif abs(self.__x - center_x) < self.__map.eps and \
                    self.__map.blocks[row + self.__y_direction()][col] == BlockType.SPACE:
                self.__x = center_x
                return True
        else:
            if self.__speed_x != 0:
                return True
            elif abs(self.__y - center_y) < self.__map.eps and \
                    self.__map.blocks[row][col + self.__x_direction()] == BlockType.SPACE:
                self.__y = center_y
                return True
        return False

    def __x_direction(self):
        return self.__intended_speed_x // self.abs_speed__

    def __y_direction(self):
        return self.__intended_speed_y // self.abs_speed__

    @property
    def circle(self):
        return Circle(self.__x, self.__y, self.__radius)

    @property
    def cur_block(self):
        return Block(self.__x, self.__y, self.__map.block_size)
