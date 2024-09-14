import sys
from collections import deque

input = sys.stdin.readline
n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
board = [[0] * n for _ in range(n)] # 보드 만들기

# 보드에서 뱀의 몸은 1, 사과는 2로 표현한다. 

for _ in range(k):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 2

info = []
l = int(input()) # 방향이 몇번 바뀌는지 (초, 방향 L:왼쪽 D:오른쪽)
for _ in range(l):
    sec, direct = input().split()
    info.append((int(sec), direct))

# 아래쪽, 오른쪽, 위쪽, 왼쪽의 방향 정보 
# 0,0이 좌상단 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
current_direction = 1 # 시작 방향은 오른쪽
current_y = current_x = 0 # 시작 위치는 좌상단 
time, i = 0, 0 # 시간과, info 리스트의 인덱스
snake = deque([(current_y, current_x)]) # 시작시 뱀의 길이는 1

while True:
    # 뱀을 현재 방향으로 진행
    current_y, current_x = current_y + dy[current_direction], current_x + dx[current_direction]
    time += 1

    # 뱀의 몸통에 닿거나 벽에 부딪히는 경우 종료
    if current_y < 0 or current_x < 0 or current_y >= n or current_x >= n or board[current_y][current_x] == 1:
        break

    # 이상없다면 해당 타일에 사과가 있는지 확인, 없다면 꼬리를 지운다.
    if board[current_y][current_x] != 2:
        tail_y, tail_x = snake.popleft()
        board[tail_y][tail_x] = 0
    
    # 이동한 위치를 뱀으로 바꾸고 뱀큐에도 넣는다
    board[current_y][current_x] = 1
    snake.append((current_y, current_x))

    # 방향을 전환해야하는 시간이라면 방향을 전환한다.
    if time == info[i][0]:
        if info[i][1] == "L": # 다음 방향이 왼쪽이라면
            current_direction = (current_direction + 1) % 4
        elif info[i][1] == "D": # 다음 방향이 오른쪽이라면
            current_direction = (4 + current_direction -1) % 4 # 인덱스가 음수가되는경우를 생각해 4를 더해줌
        
        # 인덱스가 범위를 넘지 않도록 한다. 
        if i + 1 < l:
            i += 1


print(time)