import pygame


class Animation:
    def __init__(self, frames, time_per_frame):
        self.__frames = frames
        self.__playing_time = 0
        self.__last_img = frames[0]
        self.__time_per_frame = time_per_frame
        self.__total_animation_time = len(frames) * time_per_frame

    def update(self):
        self.__playing_time = (self.__playing_time + 1) % self.__total_animation_time

    def get_image(self, x_direction, y_direction):
        cur_img = self.__frames[self.__playing_time // self.__time_per_frame]
        if x_direction == 1:
            self.__last_img = cur_img
        elif x_direction == -1:
            self.__last_img = pygame.transform.flip(cur_img, True, False)
        elif y_direction == 1:
            self.__last_img = pygame.transform.rotate(cur_img, -90)
        elif y_direction == -1:
            self.__last_img = pygame.transform.rotate(cur_img, 90)
        return self.__last_img
