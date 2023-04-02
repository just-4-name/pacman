import pygame


class Animation:
    def __init__(self, frames):
        self.__frames = frames
        self.__cur_frame = 0
        self.__last_img = frames[0]

    def next_frame(self):
        self.__cur_frame = (self.__cur_frame + 1) % len(self.__frames)

    def get_image(self, x_direction, y_direction):
        cur_img = self.__frames[self.__cur_frame]
        if x_direction == 1:
            self.__last_img = cur_img
        elif x_direction == -1:
            self.__last_img = pygame.transform.flip(cur_img, True, False)
        elif y_direction == 1:
            self.__last_img = pygame.transform.rotate(cur_img, -90)
        elif y_direction == -1:
            self.__last_img = pygame.transform.rotate(cur_img, 90)
        return self.__last_img
