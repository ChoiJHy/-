import sys
input = sys.stdin.readline

def sol(y, x):
    if floor[y][x] == '-': # - 모양 판자라면
        floor[y][x] = 0 # 방문처리, 다음번 재귀에서 다시 호출되지 않도록 

        # 왼쪽 바닥 확인 
        lx = x - 1
        if  0 <= lx and floor[y][lx] == '-': # 범위에서 벗어나지 않고 같은 글자 라면 재귀
            sol(y, lx)
        
        # 오른쪽 바닥 확인
        rx = x + 1
        if rx < m and floor[y][rx] == '-':
            sol(y, rx)
    
    if floor[y][x] == '|': # | 모양 판자라면
        floor[y][x] = 1 # 방문처리

        #위쪽 바닥 확인
        uy = y - 1
        if  0 <= uy and floor[uy][x] == '|': # 범위에서 벗어나지 않고 같은 글자 라면 재귀
            sol(uy, x)

        #아래쪽 바닥 확인
        dy = y + 1
        if dy < n and floor[dy][x] == '|':
            sol(dy, x)

n, m = map(int, input().split())

floor = [list(input()) for _ in range(n)]

# for i in range(n):
#     print(floor[i])

cnt = 0

for j in range(n):
    for i in range(m):
        if floor[j][i] == '-' or floor[j][i] == '|': # 방문처리한 노드는 다시 들어가지 않음
            sol(j, i)
            cnt += 1

print(cnt)