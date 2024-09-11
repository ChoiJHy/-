import sys

n = int(sys.stdin.readline())

# towers = [map(int, sys.stdin.readline().split()) for _ in range(n)]
towers = list(map(int, sys.stdin.readline().split()))

stack = []
ans = [0] * n

# for i in reversed(range(len(towers))):
#     is_nothing = True
#     for j in reversed(range(i)):
#         if towers[i] <= towers[j]:
#             towers[i] = j + 1
#             is_nothing = False
#             break
#     if is_nothing:
#         towers[i] = 0

for i in range(n):
    while stack:
        if stack[-1][1] > towers[i]:
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((i, towers[i]))



# print(*towers, sep=' ')


for i in range(n):
    sys.stdout.write(str(ans[i])+ " ")