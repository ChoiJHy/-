import sys
from collections import deque
input = sys.stdin.readline
INF = 1e6

n = int(input())

rooms = [list(map(int, input().rstrip())) for _ in range(n)]
costs = [[INF] * n for _ in range(n)]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]

# 코스트, y, x
queue = deque([[0, 0, 0]])
costs[0][0] = 0

while queue:
    cost, cy, cx = queue.popleft()

    if costs[cy][cx] < cost:
        continue
    
    for i in range(4):
        ny, nx = cy + dy[i], cx + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if 1 == rooms[ny][nx]:
                total_cost = cost
            elif 0 == rooms[ny][nx]:
                total_cost = cost + 1
        else:
            continue

        if total_cost < costs[ny][nx]:
            costs[ny][nx] = total_cost
            queue.append([total_cost, ny, nx])


# for i in range(n):
#     print(costs[i])

print(costs[n-1][n-1])