import sys
from collections import deque
input = sys.stdin.readline

rows, cols = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(rows)]

# 동서남북을 위한 방향 벡터
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]


def Is_Divided():
    visited = [[False] * cols for _ in range(rows)]
    pieces = 0
    
    for row in range(1, len(field)-1):
        for col in range(1,len(field[row])-1):
            if 0 < field[row][col] and not visited[row][col]:
                pieces += 1

                if 1 < pieces:
                    return pieces
                
                queue = deque([(row, col)])
                visited[row][col] = True
                while queue:
                    y, x = queue.popleft()
                    for dir in range(4):
                        nx, ny = x + dx[dir], y + dy[dir]
                        if 0 <= ny < rows and 0 <= nx < cols and not visited[ny][nx] and field[ny][nx] > 0:
                            visited[ny][nx] = True
                            queue.append((ny, nx))
    
    return pieces

years = 0
while True:

    pieces = Is_Divided()
    if 1 < pieces:
        print(years)
        break

    if 0 == pieces:
        print(0)
        break
    

    new_field = [sublist[:] for sublist in field]
    for row in range(1, len(field)-1):
        for col in range(1,len(field[row])-1):
            if 0 != field[row][col]:
                # 동서남북을 확인하며 바다와 인접해 있다면 -1, 0보다 작아지지는 않음
                if 0 == field[row - 1][col]:
                    new_field[row][col] = new_field[row][col] - 1 if 0 < new_field[row][col] else 0
                if 0 == field[row + 1][col]:
                    new_field[row][col] = new_field[row][col] - 1 if 0 < new_field[row][col] else 0
                if 0 == field[row][col - 1]:
                    new_field[row][col] = new_field[row][col] - 1 if 0 < new_field[row][col] else 0
                if 0 == field[row][col + 1]:
                    new_field[row][col] = new_field[row][col] - 1 if 0 < new_field[row][col] else 0
    # for field_rows in new_field:
    #     print(field_rows)
    field = new_field
    years += 1