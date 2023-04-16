import pygame.transform
from objects.Coins import Coins
from objects.Ghosts import Pinky, Clyde, Blinky, Inky
from resources import PATH_TO_MAP, PACMAN_IMAGES, GHOSTS_IMAGES
from objects.Map import Map, BlockType
from objects.Pacman import Pacman
from utils.Block import Block


class MapLoader:
    __pacman_images = []

    def __init__(self, block_size):
        pacman_block = clyde_block = pinky_block = blinky_block = inky_block = Block(-1, -1)
        f = open(PATH_TO_MAP, 'r')
        blocks = []
        for line in f.readlines():
            cur = []
            for block in line:
                if block == '1':
                    cur.append(BlockType.WALL)
                elif block == '0':
                    cur.append(BlockType.COIN)
                elif block == '2':
                    pacman_block = Block(len(cur), len(blocks))
                    cur.append(BlockType.COIN)
                elif block == 'P':
                    pinky_block = Block(len(cur), len(blocks))
                    cur.append(BlockType.COIN)
                elif block == 'C':
                    clyde_block = Block(len(cur), len(blocks))
                    cur.append(BlockType.COIN)
                elif block == 'B':
                    blinky_block = Block(len(cur), len(blocks))
                    cur.append(BlockType.COIN)
                elif block == 'I':
                    inky_block = Block(len(cur), len(blocks))
                    cur.append(BlockType.COIN)
            blocks.append(cur)
        self.__map = Map(blocks, block_size)
        self.__ghosts = {'pinky': Pinky(self.__map, pinky_block), 'clyde': Clyde(self.__map, clyde_block),
                         'blinky': Blinky(self.__map, blinky_block), 'inky': Inky(self.__map, inky_block)}
        self.__get_images(block_size)
        self.__pacman = Pacman(self.__map, pacman_block, self.__pacman_images)
        self.__coins = Coins(self.__map)

    def __get_images(self, block_size):
        for path in PACMAN_IMAGES:
            self.__pacman_images.append(pygame.transform.scale(pygame.image.load(path), (block_size, block_size)))
        for ghost_name, ghost in self.__ghosts.items():
            ghost.set_image(pygame.transform.scale(pygame.image.load(f'{GHOSTS_IMAGES}/{ghost_name}_img.png'),
                                                   (block_size, block_size)))

    @property
    def map(self):
        return self.__map

    @property
    def ghosts(self):
        return self.__ghosts

    @property
    def pacman(self):
        return self.__pacman

    @property
    def coins(self):
        return self.__coins
