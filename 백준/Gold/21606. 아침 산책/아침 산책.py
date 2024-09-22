import sys
input = sys.stdin.readline

# 재귀를 이용한 DFS
def DFS(v):
    # 방문한 정점 표시
    visited[v] = True
    
    count = 0

    # 들어온 정점이 실내라면 거기서 경로를 하나 찾은것
    if is_indoors[v]:
        return 1
    # 실외라면 인접한 정점들을 돌면서 실내노드를 찾는다.
    for i in graph[v]:
        if False == visited[i]:
            count += DFS(i)
    return count


n = int(input())
A = input()

is_indoors = [int(c) for c in A if c.isdigit()]
is_indoors.insert(0, 0)


visited = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0

# 실내 정점끼리 직접  연결된 경우를 카운트
for i in range(1, n + 1):
    if is_indoors[i]:
        for neighbor in graph[i]: # 인접한 정점들을 돌면서
            if is_indoors[neighbor]: # 실내 - 실내 경로라면  결로를 하나 찾은것 
                # 여기서 인접한 정점의 방문처리를 하지 않는 이유는 경로가 반대방향으로도 성립하기 때문에
                # 반복문을 돌면 결국 다시 인접한 정점을 기준으로 들어오기 때문에 상관 없다.
                answer += 1

# 실외 노드를 기준으로 DFS를 돌면서 실내 - 실내 경로를 찾음
# ex) 실외 - 실내 - 실내 - 실외
# 위 경우 경로는 단 하나이지만 
# 위 함수대로라면 실내를 만났을 때 바로 경로가 있다고 카운트를 증가시켜서  총 3개의 경로가 나올 수 있다.
# 때문에 아래에서 경로가 1개만 나왔다면 카운팅에 들어가지 않게 된다.
for i in range(1, n + 1):
    if not visited[i] and not is_indoors[i]: # 실외이면서 방문한적이 없는경우
        count_of_indoor = DFS(i)
        if count_of_indoor > 1: 
            answer += count_of_indoor * (count_of_indoor - 1) # 한 실외 정점을 기준으로 여러개의 실내가 나왔다면 만들수 있는 조합의 수는  n * (n-1)이다

print(answer)
