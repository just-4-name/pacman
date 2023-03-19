class Block:
    def __init__(self, x, y, block_size=None):
        if block_size is None:
            self.row = x
            self.col = y
        else:
            self.row = round(y) // block_size
            self.col = round(x) // block_size

    def equals(self, block):
        return self.row == block.row and self.col == block.col
