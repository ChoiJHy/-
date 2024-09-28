n, k = map(int, input().split())
items = [[0, 0] for _ in range(n + 1)] # 무게, 가치

for i in range(1, n + 1):
    items[i] = list(map(int, input().split()))

P1 = [0] * (k + 1)
for weight, value in items:
    for w in range(k, weight - 1, -1):
        P1[w] = max(P1[w], P1[w - weight] + value)

print(P1[k])