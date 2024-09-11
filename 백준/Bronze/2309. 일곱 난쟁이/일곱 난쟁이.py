# 일곱 난쟁이
import sys

height = []
sum_height = 0

finish = False
for i in range(9):
    height.append(int(sys.stdin.readline()))
    sum_height += height[-1]


sum_height -= 100

for i in range(len(height) -1):
    for j in range(i+1, len(height)):
        if sum_height == (height[i] + height[j]):
            a = height[i]
            b = height[j]
            height.remove(a)
            height.remove(b)
            finish = True
            break
    if finish:
        break

height.sort()

for i in height:
    sys.stdout.write(str(i) + '\n')