from objects.Ghost import Ghost
from resources import PATH_TO_MAP
from objects.Map import Map, BlockType
from objects.Pacman import Pacman
from utils.Block import Block


class MapLoader:
    def __init__(self, block_size):
        pacman_block = Block(-1, -1)
        ghosts_blocks = []
        f = open(PATH_TO_MAP, 'r')
        blocks = []
        for line in f.readlines():
            cur = []
            for block in line:
                if block == '1':
                    cur.append(BlockType.WALL)
                elif block == '0':
                    cur.append(BlockType.SPACE)
                elif block == '2':
                    pacman_block = Block(len(cur), len(blocks))
                    cur.append(BlockType.SPACE)
                elif block == '3':
                    ghosts_blocks.append(Block(len(cur), len(blocks)))
                    cur.append(BlockType.SPACE)
            blocks.append(cur)
        self.__map = Map(blocks, block_size)
        self.__pacman = Pacman(self.__map, pacman_block)
        self.__ghosts = []
        for block in ghosts_blocks:
            self.__ghosts.append(Ghost(self.__map, block))

    @property
    def map(self):
        return self.__map

    @property
    def ghosts(self):
        return self.__ghosts

    @property
    def pacman(self):
        return self.__pacman
