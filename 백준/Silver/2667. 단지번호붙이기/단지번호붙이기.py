import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
MAP = []
ans = []

for _ in range(n):
    MAP.append(list(map(int, input().rstrip())))

# for i in range(n):
#     print(MAP[i])


# bfs에 활용할 큐 생성
queue = deque()
# 집 개수를 샐 변수
count = 0
# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for y in range(n):
    for x in range(n):
        if 1 == MAP[y][x]: # 맵을 돌다 집을 발견했다면 
            queue.append([y, x]) # 큐에 넣고 
            MAP[y][x] = 0 # 다시 방문하지 않도록 변경 
            count += 1 # 집 개수 증가
            
            # 큐가 빌 때까지 탐색 진행
            while queue:
                cy, cx = queue.popleft()
                for i in range(4):
                    ny, nx = cy + dy[i], cx + dx[i]

                    #다음 위치가 범위를 벗어나지 않으며 집이 있는경우
                    if 0 <= ny < n and 0 <= nx < n and 1 == MAP[ny][nx]:
                        MAP[ny][nx] = 0 # 해당 집은 방문처리
                        count += 1 # 집 개수를 늘려주고
                        queue.append([ny, nx]) # 큐에 넣어준다.
            # 탐색이 끝나고 나왔다면 
            ans.append(count) # 리스트에 결과값을 넣어주고
            count = 0 # 카운트 초기화

ans.sort() # 결과를 오름차순으로 출력하기 위해서 정렬

print(len(ans))
for i in ans:
    print(i)