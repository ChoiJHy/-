import sys
input = sys.stdin.readline
num_list = [0] * 10001 # 10,000인덱스 까지 

for _ in range(int(input())):
    num_list[int(input())] += 1

for i in range(len(num_list)):
    if 0 != num_list[i]:
        for j in range(num_list[i]):
            print(i)

