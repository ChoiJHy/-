import sys
from collections import deque
import heapq
input = sys.stdin.readline
INF = 1e8

n = int(input())
m = int(input())

visited = [False] * n
costs = [INF] * n

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a-1].append((b-1, cost))

start, end = map(int, input().split())

costs[start - 1] = 0

#####################################
#       힙을 사용해서 만드는 방법 
#######################################
# heap = []
# heapq.heappush(heap,(0, start-1))

# while heap:
#     cost, current_node = heapq.heappop(heap)

#     if costs[current_node] < cost and visited[current_node]:
#         continue
#     # if costs[current_node] < cost :
#     #     continue

#     visited[current_node] = True
#     for next_node, next_cost in graph[current_node]:
#         total_cost = cost + next_cost
#         if total_cost < costs[next_node]: # 인접노드를 거쳐가는 비용이 원래 비용보다 쌀경우
#             costs[next_node] = total_cost # 최소비용갱신
#             heapq.heappush(heap, (total_cost, next_node))


#####################################
#      우선순위 큐를 사용해서 만들기
#######################################
queue = deque([[0, start - 1]])

while queue:
    cost, current_node = queue.popleft()

    if costs[current_node] < cost:
        continue

    for next_node, next_cost in graph[current_node]:
        total_cost = cost + next_cost
        if total_cost < costs[next_node]:
            costs[next_node] = total_cost
            queue.append([total_cost, next_node])
            
print(costs[end-1])