import unittest

from utils.Block import Block
from utils.MapLoader import MapLoader
from utils.PathFinder import ShortestPathFinder, manhattan_dist


class TestShortestPathFinder(unittest.TestCase):
    BLOCK_SIZE = 40

    def setUp(self):
        map_loader = MapLoader(self.BLOCK_SIZE)
        self.path_finder = ShortestPathFinder(map_loader.map)

    def test_manhattan_dist(self):
        self.assertEqual(manhattan_dist(Block(1, 3), Block(90, 130, self.BLOCK_SIZE)), 1)

    def test_path_finder(self):
        self.assertEqual(self.path_finder.get_direction(Block(2, 1), Block(4, 1)), (1, 0))
        self.assertEqual(self.path_finder.get_direction(Block(1, 2), Block(5, 4)), (0, 1))


if __name__ == "__main__":
    unittest.main()
