from objects.Map import BlockType
from utils.Block import Block
import heapq as hq


def manhattan_dist(block1, block2):
    return abs(block1.y - block2.y) + abs(block1.x - block2.x)


class ShortestPathFinder:

    def __init__(self, mapp):
        self.__map = mapp

    def get_direction(self, start, target):
        prev = self.__a_star(start, target)
        cur = target
        while prev[cur.y][cur.x] != start:
            cur = prev[cur.y][cur.x]
        return cur.x - start.x, cur.y - start.y

    def __a_star(self, start, target):
        dist = [[-1] * len(self.__map.blocks) for _ in range(len(self.__map.blocks))]
        prev = [[start] * len(self.__map.blocks) for _ in range(len(self.__map.blocks))]
        dist[start.y][start.x] = 0
        queue = []
        hq.heappush(queue, (0, start))
        while True:
            length, vertex = hq.heappop(queue)
            if vertex.is_equal(target):
                break
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (dx != 0 and dy != 0) or (dx == dy == 0):
                        continue
                    to = Block(vertex.x + dx, vertex.y + dy)
                    if not to.is_valid(len(self.__map.blocks)) or self.__map.blocks[to.y][to.x] == BlockType.WALL:
                        continue
                    new_dist = dist[vertex.y][vertex.x] + 1
                    if dist[to.y][to.x] == -1 or dist[to.y][to.x] > new_dist:
                        prev[to.y][to.x] = vertex
                        dist[to.y][to.x] = new_dist
                        hq.heappush(queue, (new_dist + manhattan_dist(to, target), to))
        return prev
