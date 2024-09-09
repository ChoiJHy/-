def findPrime(n) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1, 1):
        if n % i == 0:
            return False
    return True


caseNum = int(input())

for _ in range(caseNum):
    n = int(input())
    a = b = int(n*0.5)

    for i in range(int(n*0.5)):
        if findPrime(a) and findPrime(b):
            print(str(a) + ' ' + str(b))
            break
        a -= 1
        b += 1
