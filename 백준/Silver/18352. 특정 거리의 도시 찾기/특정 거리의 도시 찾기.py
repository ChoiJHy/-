import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split()) # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)

distance = [-1] * n # -1은 방문하지 않은 도시
distance[x-1] = 0 # 자기자신은 0

queue = deque([x-1])

while queue:
    current = queue.popleft()

    for next in graph[current]:
        if -1 == distance[next]:
            distance[next] = distance[current] + 1
            queue.append(next)


if k in distance:
    for i in range(n):
        if k == distance[i]:
            print(i+1)
else:
    print(-1)
