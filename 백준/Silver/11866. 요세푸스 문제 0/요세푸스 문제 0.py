n, k = map(int, input().split())

N = [i+1 for i in range(n)]
result = []
i = 0
while N:
    i += k - 1

    if i >= len(N):
        i %= len(N)

    result.append(str(N.pop(i)))

print("<",", ".join(result), ">", sep="")