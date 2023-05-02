from utils.Block import Block
from utils.Circle import Circle
from utils.PathFinder import ShortestPathFinder


class Ghost:
    _img = None

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

    def draw(self, screen):
        intent = self._map.block_size / 2
        screen.blit(self._img, (self._x - intent, self._y - intent))

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

    def check_collision(self, circle):
        return Circle(self._x, self._y, self._radius).intersects(circle)

    def get_cur_block(self):
        return Block(self._x, self._y, self._map.block_size)

    def set_image(self, img):
        self._img = img
