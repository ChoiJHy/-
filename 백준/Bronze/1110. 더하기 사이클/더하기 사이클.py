n = int(input())
original = n
a = n // 10
b = n % 10

new_number = (b * 10 + (a + b) % 10)

cnt = 1

while original != new_number:
    n = new_number

    a = n // 10
    b = n % 10

    new_number = (b * 10 + (a + b) % 10)
    cnt += 1


print(cnt)