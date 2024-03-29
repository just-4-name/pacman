import pygame
from world.World import World


WIDTH = World.BLOCK_SIZE * 15
HEIGHT = World.BLOCK_SIZE * 15 + 100
FPS = 60

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
            world.key_pressed(event.key)
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
