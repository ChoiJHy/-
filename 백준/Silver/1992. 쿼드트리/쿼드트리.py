import sys

def div(x, y, n):
    global result
    # 이번 사각형에서의 기준 색 
    std_color = video[y][x]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 이번 사각형의 전체가 같은색이 아닐경우
            if video[j][i] != std_color: # 사각형을 4등분 
                result += '('
                div(x, y, n//2) # 좌상단
                div(x + n//2, y, n//2) # 우상단
                div(x, y + n//2, n//2) # 좌하단
                div(x + n//2, y + n//2, n//2) # 우하단
                result += ')'
                return 
    else:
        if std_color == 0:
            result += '0'
        else:
            result += '1'


n = int(input())
temp = [input() for _ in range(n)]


video = []

for i in range(n):
    video_row = []
    for number in temp[i]:
        video_row.append(int(number))
    video.append(video_row)

# for i in range(n):
#     for number in temp[i]:
#         video.append(int(number))

result = ''


div(0, 0, n)

print(result)