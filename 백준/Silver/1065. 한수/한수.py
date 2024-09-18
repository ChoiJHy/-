num = int(input())

count = 0

for i in range(1, num+1):
    num_list = list(map(int, str(i))) # 숫자를 각 자리별로 리스트에 넣는다.
    if 100 > i:
        count += 1
    elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
        count += 1
print(count)