n = int(input())

for _ in range(n):
    result = input()
    answer = 0
    point = 0

    for c in result:
        if 'O' == c:
            point += 1
        elif 'X' == c:
            point = 0
        
        answer += point
    
    print(answer)