import pygame
from utils.MapLoader import MapLoader
from objects.Map import Singleton


class World(metaclass=Singleton):
    BLOCK_SIZE = 40
    __score = 0
    WHITE = (255, 255, 255)

    def __init__(self, screen):
        map_loader = MapLoader(self.BLOCK_SIZE)
        self.__map = map_loader.map
        self.__pacman = map_loader.pacman
        self.__screen = screen
        self.__ghosts = map_loader.ghosts
        self.__coins = map_loader.coins

    def update(self):
        self.__pacman.update(1)
        self.__screen.fill((0, 0, 0))
        for ghost in self.__ghosts.values():
            ghost.update(1, self.__pacman.cur_block, self.__pacman.x_direction(), self.__pacman.y_direction())
        self.__check_collisions()

    def draw(self):
        self.__coins.draw(self.__screen)
        for ghost in self.__ghosts.values():
            ghost.draw(self.__screen)
        self.__map.draw(self.__screen)
        self.__pacman.draw(self.__screen)
        font = pygame.font.SysFont("TimesNewRoman", 24)
        score_img = font.render("SCORE: " + str(self.__score), True, self.WHITE)
        lives_img = font.render("LIVES: " + str(self.__pacman.lives_counter), True, self.WHITE)
        self.__screen.blit(score_img, (self.BLOCK_SIZE * 0.5, self.BLOCK_SIZE * (len(self.__map.blocks) + 0.5)))
        self.__screen.blit(lives_img, (self.BLOCK_SIZE * 4, self.BLOCK_SIZE * (len(self.__map.blocks) + 0.5)))

    def update_direction(self, event_key):
        pacman_moves = {pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d}
        if event_key in pacman_moves:
            self.__pacman.update_direction(event_key)

    def to_initial_state(self):
        self.__pacman.move_to_initial_position()
        for ghost in self.__ghosts.values():
            ghost.move_to_initial_position()

    def __check_collisions(self):
        self.__pacman.check_collision()
        if self.__coins.check_collision(self.__pacman.cur_block, self.__pacman.dist_to_center()):
            self.__score += 1
        for ghost in self.__ghosts.values():
            if ghost.check_collision(self.__pacman.circle):
                self.__pacman.died()
                if not self.__pacman.is_alive():
                    print('lost')
                self.to_initial_state()
