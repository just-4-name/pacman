class Block:
    def __init__(self, x, y, block_size=None):
        if block_size is None:
            self.x = x
            self.y = y
        else:
            self.x = round(x) // block_size
            self.y = round(y) // block_size

    def is_equal(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.y > other.y if self.y != other.y else self.x > other.x

    def is_valid(self, sz):
        return 0 <= self.x < sz and 0 <= self.y < sz
