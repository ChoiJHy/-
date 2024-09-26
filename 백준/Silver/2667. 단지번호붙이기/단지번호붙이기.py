import sys
from collections import deque

# 입력
n = int(input())
# 그래프 생성
graph = [list(map(int, input().strip())) for _ in range(n)]
# 방문리스트
visited = [[False] * n for _ in range(n)]
# 4방향 탐색 키
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS---------------------------------------------------------------------------------------------------------
def BFS(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True 
                queue.append((nx, ny))
                count += 1

    return count
# ------------------------------------------------------------------------------------------------------------

# 결과값
result = []

# 탐색
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(BFS(i, j))

# 오름차순 정렬
result.sort()

# 단지의 개수
print(len(result))

# 정렬한 단지별 아파트 개수
for apartment_c in result:
    print(apartment_c)