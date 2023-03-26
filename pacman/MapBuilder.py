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
        self.__map = Map(blocks, block_size)
        self.__ghosts = [Ghost(60, 260, self.__map)]

    @property
    def map(self):
        return self.__map

    @property
    def ghosts(self):
        return self.__ghosts
