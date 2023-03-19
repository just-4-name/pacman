import pygame
from World import World


WIDTH = 480
HEIGHT = 480
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()

world = World(screen)
running = True
while running:
    clock.tick(FPS)
    pygame.display.flip()
    world.update()
    world.draw()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            world.update_direction(event.key)
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
