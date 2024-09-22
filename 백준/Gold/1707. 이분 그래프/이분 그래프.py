import sys
from collections import deque
input = sys.stdin.readline


# 함수는 BSF와 똑같지만 조건의 체크에서 인접 노드끼리의 그릅 비교가 들어간다.
def solution(start, group):
    queue = deque([start])
    group_list[start] = group

    while queue:
        vertex = queue.popleft()

        for i in graph[vertex]:
            if not group_list[i]:
                queue.append(i)
                group_list[i] = -group_list[vertex] # 인접 노드와 반대 그룹으로 설정
            elif group_list[i] == group_list[vertex]:
                return False
    
    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b  = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    group_list = [0] * (v + 1)


   # 이어져 있지 않은 정점이 있을 수 있기 때문에 모든 정점에 대해서 BFS를 돌려본다.
    for i in range(1, v + 1):
        if not group_list[i]:
            if False == solution(i, 1):
                print("NO")
                break
    else:
        print("YES")
            
