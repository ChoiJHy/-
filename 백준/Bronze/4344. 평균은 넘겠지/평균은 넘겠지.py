n = int(input())

for _ in range(n):
    scores = list(map(int, input().split()))
    average = sum(scores[1:]) / scores[0]

    count = 0
    for i in scores[1:]:
        if i > average:
            count += 1
    
    print('%.3f' %((count / scores[0]) * 100) + '%')