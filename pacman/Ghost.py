from collections import deque
from Map import *
from Block import Block
from Circle import Circle


class Ghost:
    Red = (255, 0, 0)

    def __init__(self, x, y, mapp):
        self.__x = x
        self.__y = y
        self.__map = mapp
        self.__speed_x = self.__speed_y = 0
        self.__abs_speed = 1
        self.__radius = mapp.block_size / 2

    def update(self, dt, target):
        self.__bfs(target)
        self.__x += self.__speed_x * dt
        self.__y += self.__speed_y * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.Red, (self.__x, self.__y), self.__radius)

    def __bfs(self, target):
        queue = deque()
        start = Block(self.__x, self.__y, self.__map.block_size)
        queue.append(start)
        dist = [[2 * self.__map.block_size] * len(self.__map.blocks[0]) for _ in range(len(self.__map.blocks))]
        prev = [[Block(-1, -1)] * len(self.__map.blocks[0]) for _ in range(len(self.__map.blocks))]
        dist[start.row][start.col] = 0
        while True:
            cur = queue.popleft()
            cur_dist = dist[cur.row][cur.col]
            if cur.equals(target):
                break
            if cur.row > 0 and self.__map.blocks[cur.row - 1][cur.col] == BlockType.space \
                    and dist[cur.row - 1][cur.col] > cur_dist + 1:
                dist[cur.row - 1][cur.col] = cur_dist + 1
                prev[cur.row - 1][cur.col] = cur
                queue.append(Block(cur.row - 1, cur.col))
            if cur.row + 1 < len(self.__map.blocks) and self.__map.blocks[cur.row + 1][cur.col] == BlockType.space \
                    and dist[cur.row + 1][cur.col] > cur_dist + 1:
                dist[cur.row + 1][cur.col] = cur_dist + 1
                prev[cur.row + 1][cur.col] = cur
                queue.append(Block(cur.row + 1, cur.col))
            if cur.col > 0 and self.__map.blocks[cur.row][cur.col - 1] == BlockType.space \
                    and dist[cur.row][cur.col - 1] > cur_dist + 1:
                dist[cur.row][cur.col - 1] = cur_dist + 1
                prev[cur.row][cur.col - 1] = cur
                queue.append(Block(cur.row, cur.col - 1))
            if cur.col + 1 < len(self.__map.blocks) and self.__map.blocks[cur.row][cur.col + 1] == BlockType.space \
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
        center_x = self.__map.block_size * (start.col + 0.5)
        center_y = self.__map.block_size * (start.row + 0.5)
        self.__speed_x = self.__speed_y = 0
        if dy != 0:
            if abs(self.__x - center_x) > self.__map.block_size / 16:
                self.__speed_x = self.__abs_speed if center_x > self.__x else -self.__abs_speed
            else:
                self.__x = center_x
                self.__speed_y = dy * self.__abs_speed
        else:
            if abs(self.__y - center_y) > self.__map.block_size / 16:
                self.__speed_y = self.__abs_speed if center_y > self.__y else -self.__abs_speed
            else:
                self.__y = center_y
                self.__speed_x = dx * self.__abs_speed

    def check_collision(self, circle):
        return Circle(self.__x, self.__y, self.__radius).intersects(circle)
