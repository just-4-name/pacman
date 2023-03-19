from Ghost import *


class MapBuilder:
    def __init__(self, block_size):
        # TODO map and ghosts generation
        f = open('map.txt', 'r')
        blocks = []
        for line in f.readlines():
            cur = []
            for block in line:
                if block == '*':
                    cur.append(BlockType.wall)
                elif block == '.':
                    cur.append(BlockType.space)
            blocks.append(cur)
        self.__map__ = Map(blocks, block_size)
        self.__ghosts__ = [Ghost(60, 260, self.__map__)]

    def get_map(self):
        return self.__map__

    def get_ghosts(self):
        return self.__ghosts__
