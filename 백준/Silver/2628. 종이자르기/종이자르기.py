x, y = map(int, input().split()) # 종이의 크기
# 자를 점을 넣을 리스트, 길이를 구할 때 사용함
x_list = [0, x]
y_list = [0 ,y] 

for _ in range(int(input())):
    distance, point = map(int, input().split())
    # 가로 방향으로 자르면 세로의 길이에 영향을 주므로 y_list에 넣는다.
    if 0 == distance:
        y_list.append(point)
    else: # 세로 방향으로 자르면 가로의 길이에 영향을 주므로 x_list에 넣는다.
        x_list.append(point)

# 좌상단부터 차례대로 사각형의 크기를 구하기 위해서 오름차순 정렬
x_list.sort()
y_list.sort()

max_square = 0
for i in range(1, len(y_list)):
    for j in range(1, len(x_list)):
        width = x_list[j] - x_list[j-1] # 가로의 길이를 구함. 오름차순 정렬을 했기때문에 항상 양수
        height = y_list[i] - y_list[i-1] # 세로의 길이를 구함
        max_square = max(max_square, width * height)

print(max_square)