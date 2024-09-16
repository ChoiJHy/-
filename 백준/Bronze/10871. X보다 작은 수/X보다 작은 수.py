n, x = map(int, input().split())

array = list(map(int, input().split()))
result = []

for i in range(len(array)):
    if(array[i] < x):
        result.append(array[i])

print(*result)