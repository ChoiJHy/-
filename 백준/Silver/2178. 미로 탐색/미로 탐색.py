import sys
from collections import deque
input = sys.stdin.readline

def sol(y, x):
    queue = deque([(y, x)])

    while queue:
        oy, ox = queue.popleft()

        for i in range(4):
            nx = ox + dx[i]
            ny = oy + dy[i]

            if 0 <= nx < m and 0 <= ny < n and maze[ny][nx] == 1:
                queue.append((ny, nx))
                maze[ny][nx] += maze[oy][ox]

    return maze[n-1][m-1]



n, m = map(int, input().split())

maze = []

for _ in range(n):
    maze.append((list(map(int, input().strip('\n')))))

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# for y in range(n):
#     for x in range(m):
#         print(maze[y][x], end='')
#     print()

print(sol(0, 0))
