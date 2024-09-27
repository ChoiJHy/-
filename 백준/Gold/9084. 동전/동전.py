import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    counts = [0] * (m + 1) # 각 돈을 만들 수 있는 경우의 수 
    counts[0] = 1 # 0원은 언제나 만들 수 있다.
    for coin in coins:
        for money in range(m+1):
            if money >= coin: # 만들어야 하는 돈이 현재 동전의 가치 이상이라면
                counts[money] += counts[money - coin] # 금액에서 동전의 가치를 뺀 금액을 만들수 있는 경우의 수를 더해준다.
    print(counts[m])