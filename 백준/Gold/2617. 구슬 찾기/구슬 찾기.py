n, m = map(int, input().split())

# arr[i][j] i번 구슬이, j번 구슬보다 무겁다는 의미입니다.
arr = [[0] * n for _ in range(n)] # 인접행렬 행성

for _ in range(m):
    heavy, light = map(int, input().split())
    arr[heavy - 1][light - 1] = 1 # 1이라면 heavy가 light보다 무겁습니다.


# 플로이드-워셜 알고리즘을 통해서 각 정점의 무계관계를 정합니다.
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] and arr[k][j]: # i가 k보다 무겁고, k가 j보다 무겁다면 i는 j보다 무겁습니다.
                arr[i][j] = 1


# 중간이 될 수 없는 구슬의 개수를 구합니다.
count = 0

for i in range(n):
    heavier_count = 0
    lighter_count = 0
    for j in range(n):
        if arr[i][j]:
            heavier_count += 1 # i번 구슬보다 무거운 구슬의 수
        if arr[j][i]:
            lighter_count += 1 # i번 구슬보다 가벼운 구슬의 수
    
    if heavier_count >= (n + 1)/2 or lighter_count >= (n + 1)/2:
        count += 1

print(count)