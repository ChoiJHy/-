import sys
from collections import deque
input = sys.stdin.readline

def BFS(graph, v, visited):
    # 큐를 만들어주고 시작 정점을 넣어준다.
    queue = deque([v])
    visited[v] = True

    count = 0
    while queue:
        # 오름차순 정렬이기 때문에 왼쪽 부터 꺼내야 작은 수부터 들어간다.
        # 양방향 큐이기 때문에 왼쪽부터 꺼내도 성능의 문제는 없다.
        vertex = queue.popleft() 
        # sys.stdout.write(str(vertex) + ' ')

        for i in graph[vertex]:
            if False == visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    return count


n = int(input())
m = int(input())

# 정점의 번호와 인덱스를 일치시키기 위해서 들어온 개수보다 1 증가시켜서 만든다.
# 인접 리스트를 활용
graph = [ [] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    start, end = map(int, input().split())
    # 무향 그래프이기 때문에 양쪽 모두 넣어 준다.
    graph[start].append(end)
    graph[end].append(start)

# # 정점 번호가 작은 것을 먼저 방문해야 하기 때문에, 인접 리스트를 오름차순으로 정렬한다.
# for i in range(n+1):
#     graph[i].sort()


sys.stdout.write(str(BFS(graph, 1, visited)) + '\n')