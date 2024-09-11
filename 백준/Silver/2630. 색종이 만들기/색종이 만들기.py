# 색종이 만들기 문제
import sys

def div(x, y, n):
    global cnt_0, cnt_1
    # 이번 사각형에서의 기준 색 
    std_color = paper[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 이번 사각형의 전체가 같은색이 아닐경우
            if paper[i][j] != std_color: # 사각형을 4등분 
                div(x, y, n//2) # 좌상단
                div(x + n//2, y, n//2) # 우상단
                div(x, y + n//2, n//2) # 좌하단
                div(x + n//2, y + n//2, n//2) # 우하단
                return 
    else:
        if std_color == 0:
            cnt_0 += 1
        else:
            cnt_1 += 1


n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt_0 = cnt_1 = 0

div(0, 0, n)

print(cnt_0)
print(cnt_1)