# BFS를 사용하고 방문할때마다 부모를 저장하게함 
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

# 인접 리스트 형태로 간선 정보를 받음 
graph = [[] for _ in range(n + 1)]
for i in range(n-1):
    a, b  = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = [0] * (n+1)

def BFS(start):
    queue = deque([start])

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if 0 == parents[i]:
                parents[i] = v
                queue.append(i)

BFS(1)
answer = parents[2:]

for x in answer:
    print(x)