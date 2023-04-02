from math import hypot


class Circle:
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad

    def intersects(self, other):
        return hypot(self.x - other.x, self.y - other.y) < self.rad + other.rad
