n, k = map(int, input().split())
items = [[0, 0] for _ in range(n + 1)] # 무게, 가치

for i in range(1, n + 1):
    items[i] = list(map(int, input().split()))

# n개의 물건과 배낭의 최대 무게k로 만들 수 있는 최대이익을 담을 리스트
P = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(len(P)):
    for w in range(len(P[i])):
        if items[i][0] > w: # i번째 물건의 무게가 현재 무게보다 무거우면 (추가할 수 없음)
           P[i][w] = P[i-1][w] # 이전 물건들의 가치의 합이 현재 물건까지 가치의 합
        else: # i번째 물건의 가치 + i번째 물건이 들어갈 수 있는 무게의 최대 가치 와 이전 물건까지의 최대가치를 비교해서
              # 큰 쪽을 w무게의 배낭에 i번째 물건까지의 최대가치로 한다.
            P[i][w] = max((items[i][1] + P[i-1][w - items[i][0]]), P[i-1][w])

print(P[n][k]) 