def Remainder(a, b, c):
    if b == 1:
        return a % c
    else:
        temp = Remainder(a, b//2, c)
        if b % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c


a, b, c = map(int, input().split())

Remainder(a, b, c)

print(Remainder(a, b, c))