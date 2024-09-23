A = int(input())
B = list(map(int,input().split()))
C = list(map(int,input().split()))

Maximum = -1e9
Minimum = 1e9 


def solution(depth,count,add,sub,mul,div):
     global Maximum,Minimum
     if depth == A:
          Maximum = max(count,Maximum)
          Minimum = min(count,Minimum)

          return
     if add:
          solution(depth+1,count+B[depth],add-1,sub,mul,div)
     if sub:
          solution(depth+1,count-B[depth],add,sub-1,mul,div)
     if mul:
          solution(depth+1,count*B[depth],add,sub,mul-1,div)
     if div:
          solution(depth+1,int(count/B[depth]),add,sub,mul,div-1)


solution(1,B[0],C[0],C[1],C[2],C[3])
print(Maximum)
print(Minimum)