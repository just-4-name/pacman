import pygame

from objects.Coins import PickedWhat
from utils.MapLoader import MapLoader
from objects.Map import Singleton
from world.menu import Menu
from utils.GameStatus import GameStatus


class World(metaclass=Singleton):
    BLOCK_SIZE = 40
    __score = 0
    __INTERVAL_IN_KILLER_MODE = 200
    WHITE = (255, 255, 255)

    def __init__(self, screen):
        map_loader = MapLoader(self.BLOCK_SIZE)
        self.__map = map_loader.map
        self.__pacman = map_loader.pacman
        self.__screen = screen
        self.__ghosts = map_loader.ghosts
        self.__coins = map_loader.coins
        self.__menu = Menu(screen, self.__map.block_size, len(self.__map.blocks))
        self.__state = GameStatus.RUNNING
        self.__in_killer_mode = False
        self.__time_in_km = 0
        self.__max_time_in_km = 0

    def update(self):
        if self.__state != GameStatus.RUNNING:
            return
        if self.__in_killer_mode:
            self.__time_in_km += 1
            if self.__time_in_km >= self.__max_time_in_km:
                self.__max_time_in_km = 0
                self.__time_in_km = 0
                self.__in_killer_mode = False
        self.__pacman.update(1)
        self.__screen.fill((0, 0, 0))
        for ghost in self.__ghosts.values():
            if self.__in_killer_mode:
                ghost.update_in_killer_mode(self.__pacman.cur_block, 1)
            else:
                ghost.update(1, self.__pacman.cur_block, self.__pacman.x_direction(), self.__pacman.y_direction())
        self.__check_collisions()
        if self.__coins.check_if_won(self.__score):
            self.__state = GameStatus.IN_START_MENU
            self.__menu.game_won()

    def draw(self):
        if self.__state != GameStatus.RUNNING:
            return
        self.__coins.draw(self.__screen)
        for ghost in self.__ghosts.values():
            ghost.draw(self.__screen, self.__in_killer_mode)
        self.__map.draw(self.__screen)
        self.__pacman.draw(self.__screen)

        font = pygame.font.SysFont("TimesNewRoman", 24)
        score_img = font.render("SCORE: " + str(self.__score), True, self.WHITE)
        lives_img = font.render("LIVES: " + str(self.__pacman.lives_counter), True, self.WHITE)
        self.__screen.blit(score_img, (self.BLOCK_SIZE * 0.5, self.BLOCK_SIZE * (len(self.__map.blocks) + 0.5)))
        self.__screen.blit(lives_img, (self.BLOCK_SIZE * 4, self.BLOCK_SIZE * (len(self.__map.blocks) + 0.5)))

    def key_pressed(self, event_key):
        pacman_moves = {pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d}
        if event_key in pacman_moves:
            self.__pacman.update_direction(event_key)
        if event_key == pygame.K_ESCAPE:
            self.__state = GameStatus.PAUSED
            self.__menu.game_paused()
        if event_key == pygame.K_SPACE:
            if self.__state == GameStatus.IN_START_MENU:
                self.__restart()
            self.__state = GameStatus.RUNNING

    def __to_initial_state(self):
        self.__pacman.move_to_initial_position()
        for ghost in self.__ghosts.values():
            ghost.move_to_initial_position()

    def __restart(self):
        self.__to_initial_state()
        self.__score = 0
        self.__time_in_km = self.__max_time_in_km = 0
        self.__in_killer_mode = False
        self.__pacman.restore_lives_counter()
        self.__coins.restore_coins()

    def __check_collisions(self):
        self.__pacman.check_collision()
        picked = self.__coins.check_collision(self.__pacman.cur_block, self.__pacman.dist_to_center())
        if picked != PickedWhat.NOTHING:
            self.__score += 1
            if picked == PickedWhat.KILLER_COIN:
                self.__in_killer_mode = True
                self.__max_time_in_km += self.__INTERVAL_IN_KILLER_MODE
        for ghost in self.__ghosts.values():
            if ghost.check_collision(self.__pacman.circle):
                if not self.__in_killer_mode:
                    self.__pacman.died()
                    if not self.__pacman.is_alive():
                        self.__state = GameStatus.IN_START_MENU
                        self.__menu.game_lost()
                    self.__to_initial_state()
                else:
                    ghost.died(self.__pacman.cur_block)
