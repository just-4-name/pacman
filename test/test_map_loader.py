import unittest

from utils.Block import Block
from utils.MapLoader import MapLoader


class TestMapLoader(unittest.TestCase):
    BLOCK_SIZE = 40

    def setUp(self):
        self.map_loader = MapLoader(self.BLOCK_SIZE)

    def test_ghosts(self):
        self.assertEqual(len(self.map_loader.ghosts), 4)
        self.assertTrue(self.map_loader.ghosts['pinky'].get_cur_block().is_equal(Block(2, 13)))

    def test_pacman(self):
        pacman = self.map_loader.pacman
        pacman.move_to_initial_position()
        self.assertTrue(pacman.cur_block.is_equal(Block(2, 1)))

    def test_map(self):
        self.assertEqual(len(self.map_loader.map.blocks), 15)
        self.assertEqual(self.map_loader.map.eps, 4)
        self.assertEqual(self.map_loader.map.block_size, self.BLOCK_SIZE)


if __name__ == "__main__":
    unittest.main()
