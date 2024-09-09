

def hanoi(num, one, two, three):
    
    if num == 1 :
        print(one, three)

    else:
        hanoi(num - 1, one, three, two)
        print(one, three)
        hanoi(num - 1, two, one, three)


n = int(input())

one = '1'
two  = '2'
three = '3'


print(2**n - 1)

if n <= 20:
    hanoi(n, one, two, three)
