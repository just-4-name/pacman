from objects.Ghost import Ghost
from utils.Block import Block
from utils.BlockType import BlockType
from utils.PathFinder import manhattan_dist


class Pinky(Ghost):
    def update(self, dt, target, x_direction, y_direction):
        new_target = Block(target.x + x_direction * 2, target.y + y_direction * 2)
        if not new_target.is_valid(len(self._map.blocks)) or \
                self._map.blocks[new_target.y][new_target.x] == BlockType.WALL:
            new_target = Block(target.x + x_direction, target.y + y_direction)
            if self._map.blocks[new_target.y][new_target.x] == BlockType.WALL:
                new_target = target
        self._update_direction(new_target)
        self._x += self._speed_x * dt
        self._y += self._speed_y * dt


class Inky(Ghost):
    pass


class Blinky(Ghost):
    def update(self, dt, target, x_direction, y_direction):
        new_target = Block(target.x - x_direction * 2, target.y - y_direction * 2)
        if not new_target.is_valid(len(self._map.blocks)) or \
                self._map.blocks[new_target.y][new_target.x] == BlockType.WALL:
            new_target = Block(target.x - x_direction, target.y - y_direction)
            if self._map.blocks[new_target.y][new_target.x] == BlockType.WALL:
                new_target = target
        self._update_direction(new_target)
        self._x += self._speed_x * dt
        self._y += self._speed_y * dt


class Clyde(Ghost):
    DIST_FOR_WEIRD_DIRECTION = 10

    def __init__(self, mapp, block):
        super().__init__(mapp, block)
        self._speed_x = self._abs_speed

    def update(self, dt, target, x_direction, y_direction):
        dist = manhattan_dist(self.get_cur_block(), target)
        if dist > self.DIST_FOR_WEIRD_DIRECTION:
            self._update_direction(target)
        else:
            if self._map.blocks[self.get_cur_block().y][self.get_cur_block().x] == BlockType.WALL or \
                    (self._map.blocks[self.get_cur_block().y + self._speed_y // self._abs_speed]
                     [self.get_cur_block().x + self._speed_x // self._abs_speed] == BlockType.WALL and
                     self.dist_to_next_block_center() < self._map.block_size - self._map.eps) or \
                    (self._speed_x == self._speed_y == 0):
                cur_block = self.get_cur_block()
                self._x = (cur_block.x + 0.5) * self._map.block_size
                self._y = (cur_block.y + 0.5) * self._map.block_size
                self.chase_random_target()
        self._x += self._speed_x * dt
        self._y += self._speed_y * dt

    def chase_random_target(self):
        try_target = super()._get_random_free_block()
        self._update_direction(try_target)

    def dist_to_next_block_center(self):
        next_block = Block(self.get_cur_block().x + self._speed_x // self._abs_speed,
                           self.get_cur_block().y + self._speed_y // self._abs_speed)
        center_x = (next_block.x + 0.5) * self._map.block_size
        center_y = (next_block.y + 0.5) * self._map.block_size
        return abs(center_x - self._x) + abs(center_y - self._y)
