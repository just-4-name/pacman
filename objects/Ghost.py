from random import randrange

from utils.Block import Block
from utils.BlockType import BlockType
from utils.Circle import Circle
from utils.PathFinder import ShortestPathFinder


class Ghost:
    _img = None
    _killer_mode_img = None

    def __init__(self, mapp, block):
        self._initial_x = mapp.block_size * (block.x + 0.5)
        self._initial_y = mapp.block_size * (block.y + 0.5)
        self._x = self._initial_x
        self._y = self._initial_y
        self._map = mapp
        self._speed_x = self._speed_y = 0
        self._abs_speed = 1
        self._radius = mapp.block_size / 2

    def move_to_initial_position(self):
        self._x = self._initial_x
        self._y = self._initial_y

    def update(self, dt, target, x_direction, y_direction):
        self._update_direction(target)
        self._x += self._speed_x * dt
        self._y += self._speed_y * dt

    def draw(self, screen, in_killer_mode):
        intent = self._map.block_size / 2
        screen.blit(self._killer_mode_img if in_killer_mode else self._img, (self._x - intent, self._y - intent))

    def _update_direction(self, target):
        path_finder = ShortestPathFinder(self._map)
        dx, dy = path_finder.get_direction(self.get_cur_block(), target)
        center_x = self._map.block_size * (self.get_cur_block().x + 0.5)
        center_y = self._map.block_size * (self.get_cur_block().y + 0.5)
        self._speed_x = self._speed_y = 0
        if dy != 0:
            if abs(self._x - center_x) > self._map.eps:
                self._speed_x = self._abs_speed if center_x > self._x else -self._abs_speed
            else:
                self._x = center_x
                self._speed_y = dy * self._abs_speed
        else:
            if abs(self._y - center_y) > self._map.eps:
                self._speed_y = self._abs_speed if center_y > self._y else -self._abs_speed
            else:
                self._y = center_y
                self._speed_x = dx * self._abs_speed

    def update_in_killer_mode(self, pacman_block, dt):
        half_blocks = len(self._map.blocks) // 2
        target_x = 1 if pacman_block.x >= half_blocks else len(self._map.blocks) - 2
        target_y = 1 if pacman_block.y >= half_blocks else len(self._map.blocks) - 2
        self._update_direction(Block(target_x, target_y))
        self._x += self._speed_x * dt
        self._y += self._speed_y * dt

    def check_collision(self, circle):
        return Circle(self._x, self._y, self._radius).intersects(circle)

    def get_cur_block(self):
        return Block(self._x, self._y, self._map.block_size)

    def set_image(self, img):
        self._img = img

    def set_killer_img(self, img):
        self._killer_mode_img = img

    def _get_random_free_block(self):
        while True:
            try_target = Block(randrange(len(self._map.blocks)), randrange(len(self._map.blocks)))
            if try_target.is_valid(len(self._map.blocks)) and self._map.blocks[try_target.y][try_target.x] != \
                    BlockType.WALL:
                break
        return try_target

    def died(self, pacman_block):
        while True:
            try_target = self._get_random_free_block()
            if not try_target.is_equal(pacman_block):
                break
        self._x = (try_target.x + 0.5) * self._map.block_size
        self._y = (try_target.y + 0.5) * self._map.block_size
