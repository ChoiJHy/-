N, r, c = map(int, input().split())

def sol(N, r, c):

    if 0 == N:
        return 0
    
    return 2 * (r%2) + (c%2) + 4 * sol(N-1, r//2, c//2)
# 2 * (r%2) + (c%2)는 N = 0일때의 인덱스, 사분면이 커질수록 4배수임을 이용 

print(sol(N, r, c))
