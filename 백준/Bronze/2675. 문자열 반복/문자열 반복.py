testNum = int(input())

for t in range(testNum):
    r, s = input().split()
    r = int(r)
    str = ''

    for i in s:
        str += i * r

    print(str)
