def findPrime(n) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1, 1):
        if n % i == 0:
            return False
    return True
    

a = int(input())
count = 0
n = list(map(int,input().split()))
for i in range(len(n)):
    if findPrime(n[i]):
        count += 1

print(count)