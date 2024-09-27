n = int(input())

results = [0] * 1000001
results[1] = 1
results[2] = 2

for i in range(3, n+1):
    results[i] = (results[i - 1] + results[i - 2]) % 15746
print(results[n])