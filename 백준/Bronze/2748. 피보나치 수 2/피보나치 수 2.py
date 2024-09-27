import sys
input = sys.stdin.readline

n = int(input())

fibo = []
fibo.append(0)
fibo.append(1)

if 2 <= n:
    for i in range(1, n):
        fibo.append(fibo[i-1] + fibo[i])
    print(fibo[n])
elif 1 == n:
    print(fibo[1])
elif 0 == n:
    print(fibo[0])