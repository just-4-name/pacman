from collections import deque
from Map import *
from pacman.Block import Block


class Ghost:
    Red = (255, 0, 0)

    def __init__(self, x, y, mapp):
        self.__x__ = x
        self.__y__ = y
        self.__map__ = mapp
        self.__speed_x__ = self.__speed_y__ = 0
        self.__abs_speed__ = 1

    def update(self, dt, target):
        self.__bfs__(target)
        self.__x__ += self.__speed_x__ * dt
        self.__y__ += self.__speed_y__ * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.Red, (self.__x__, self.__y__), self.__map__.block_size / 2)

    def __bfs__(self, target):
        queue = deque()
        start = Block(self.__x__, self.__y__, self.__map__.block_size)
        queue.append(start)
        dist = [[2 * self.__map__.block_size] * len(self.__map__.blocks[0]) for _ in range(len(self.__map__.blocks))]
        prev = [[Block(-1, -1)] * len(self.__map__.blocks[0]) for _ in range(len(self.__map__.blocks))]
        dist[start.row][start.col] = 0
        while True:
            cur = queue.popleft()
            cur_dist = dist[cur.row][cur.col]
            if cur.equals(target):
                break
            if cur.row > 0 and self.__map__.blocks[cur.row - 1][cur.col] == BlockType.space \
                    and dist[cur.row - 1][cur.col] > cur_dist + 1:
                dist[cur.row - 1][cur.col] = cur_dist + 1
                prev[cur.row - 1][cur.col] = cur
                queue.append(Block(cur.row - 1, cur.col))
            if cur.row + 1 < len(self.__map__.blocks) and self.__map__.blocks[cur.row + 1][cur.col] == BlockType.space \
                    and dist[cur.row + 1][cur.col] > cur_dist + 1:
                dist[cur.row + 1][cur.col] = cur_dist + 1
                prev[cur.row + 1][cur.col] = cur
                queue.append(Block(cur.row + 1, cur.col))
            if cur.col > 0 and self.__map__.blocks[cur.row][cur.col - 1] == BlockType.space \
                    and dist[cur.row][cur.col - 1] > cur_dist + 1:
                dist[cur.row][cur.col - 1] = cur_dist + 1
                prev[cur.row][cur.col - 1] = cur
                queue.append(Block(cur.row, cur.col - 1))
            if cur.col + 1 < len(self.__map__.blocks) and self.__map__.blocks[cur.row][cur.col + 1] == BlockType.space \
                    and dist[cur.row][cur.col + 1] > cur_dist + 1:
                dist[cur.row][cur.col + 1] = cur_dist + 1
                prev[cur.row][cur.col + 1] = cur
                queue.append(Block(cur.row, cur.col + 1))
        cur = target
        dx = dy = 0
        while not prev[cur.row][cur.col].equals(Block(-1, -1)):
            dy = cur.row - prev[cur.row][cur.col].row
            dx = cur.col - prev[cur.row][cur.col].col
            cur = prev[cur.row][cur.col]
        center_x = self.__map__.block_size * (start.col + 0.5)
        center_y = self.__map__.block_size * (start.row + 0.5)
        self.__speed_x__ = self.__speed_y__ = 0
        if dy != 0:
            if abs(self.__x__ - center_x) > self.__map__.block_size / 16:
                self.__speed_x__ = self.__abs_speed__ if center_x > self.__x__ else -self.__abs_speed__
            else:
                self.__x__ = center_x
                self.__speed_y__ = dy * self.__abs_speed__
        else:
            if abs(self.__y__ - center_y) > self.__map__.block_size / 16:
                self.__speed_y__ = self.__abs_speed__ if center_y > self.__y__ else -self.__abs_speed__
            else:
                self.__y__ = center_y
                self.__speed_x__ = dx * self.__abs_speed__
