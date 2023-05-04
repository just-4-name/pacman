import unittest

import pygame

from objects.Coins import PickedWhat
from objects.Ghost import Ghost
from utils.Block import Block
from utils.Circle import Circle
from utils.MapLoader import MapLoader


class TestCollisions(unittest.TestCase):
    BLOCK_SIZE = 40

    def setUp(self):
        map_loader = MapLoader(self.BLOCK_SIZE)
        self.map = map_loader.map
        self.pacman = map_loader.pacman
        self.coins = map_loader.coins

    def test_pacman_ghost_collision_true(self):
        ghost = Ghost(self.map, self.pacman.cur_block)
        self.assertTrue(ghost.check_collision(self.pacman.circle))

    def test_pacman_ghost_collision_false(self):
        ghost = Ghost(self.map, Block(self.pacman.cur_block.x + 1, self.pacman.cur_block.y + 2))
        self.assertFalse(ghost.check_collision(self.pacman.circle))

    def test_circle_intersection_true(self):
        circle1 = Circle(10, 10, self.BLOCK_SIZE)
        circle2 = Circle(15, 15, self.BLOCK_SIZE)
        self.assertTrue(circle1.intersects(circle2))

    def test_circle_intersection_false(self):
        circle1 = Circle(0, 0, self.BLOCK_SIZE)
        circle2 = Circle(2 * self.BLOCK_SIZE, 2 * self.BLOCK_SIZE, self.BLOCK_SIZE)
        self.assertFalse(circle1.intersects(circle2))

    def test_pacman_does_not_go_into_wall(self):
        initial_x_dir = self.pacman.x_direction()
        initial_y_dir = self.pacman.y_direction()
        self.pacman.update_direction(pygame.K_w)
        self.pacman.update(1)
        self.assertEqual(self.pacman.y_direction(), initial_y_dir)
        self.assertEqual(self.pacman.x_direction(), initial_x_dir)

    def test_pacman_can_go_into_free_block(self):
        self.pacman.update_direction(pygame.K_a)
        self.pacman.update(1)
        self.assertEqual(self.pacman.y_direction(), 0)
        self.assertEqual(self.pacman.x_direction(), -1)

    def test_pacman_wall_collision(self):
        self.pacman.move_to_initial_position()
        self.pacman.update_direction(pygame.K_a)
        for i in range(2 * self.BLOCK_SIZE):
            self.pacman.update(1)
            self.pacman.check_collision()
        self.assertEqual(self.pacman.x_direction(), 0)
        self.assertEqual(self.pacman.y_direction(), 0)
        self.assertTrue(abs(self.pacman.circle.x - 1.5 * self.BLOCK_SIZE) < self.map.eps)
        self.assertTrue(abs(self.pacman.circle.y - 1.5 * self.BLOCK_SIZE) < self.map.eps)

    def test_pacman_coin_collision(self):
        self.assertEqual(self.coins.check_collision(self.pacman.cur_block, self.pacman.dist_to_center()),
                         PickedWhat.COIN)
        self.pacman.move_to_initial_position()
        self.assertEqual(self.coins.check_collision(self.pacman.cur_block, self.BLOCK_SIZE / 2),
                         PickedWhat.NOTHING)


if __name__ == "__main__":
    unittest.main()
