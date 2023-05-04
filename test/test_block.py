import unittest

from utils.Block import Block


class TestBlock(unittest.TestCase):
    BLOCK_SIZE = 40

    def test_equal(self):
        self.assertTrue(Block(4, 4).is_equal(Block(self.BLOCK_SIZE * 4, self.BLOCK_SIZE * 4.123421, self.BLOCK_SIZE)))
        self.assertFalse(Block(2, 2).is_equal(Block(self.BLOCK_SIZE * 3.011, self.BLOCK_SIZE * 2, self.BLOCK_SIZE)))

    def test_valid(self):
        self.assertTrue(Block(1, 1).is_valid(2))
        self.assertFalse(Block(1, 1).is_valid(1))


if __name__ == "__main__":
    unittest.main()
