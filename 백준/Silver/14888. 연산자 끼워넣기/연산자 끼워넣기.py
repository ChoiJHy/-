import sys
input = sys.stdin.readline

def Make_Operator_Combinations(add, sub, mul, div):
    stack = [([], add, sub, mul, div)] # 스택을 초기화함(path, 연산자들)
    operator_combinations = [] # 최종결과를 저장할 리스트

    while stack:
        path, add_left, sub_left, mul_left, div_left = stack.pop()

        # 모든 연산자를 사용한 경우
        if 0 == add_left and 0 == sub_left and 0 == mul_left and 0 == div_left:
            operator_combinations.append(path)
            continue

        # 덧셈 연산자를 사용할 수 있는 경우
        if 0 < add_left:
            stack.append((path + ['+'], add_left - 1, sub_left, mul_left, div_left))

        # 뺄샘 연산자를 사용할 수 있는 경우
        if 0 < sub_left:
            stack.append((path + ['-'], add_left, sub_left - 1, mul_left, div_left))
        
        # 곱셈 연산자를 사용할 수 있는 경우
        if 0 < mul_left:
            stack.append((path + ['*'], add_left, sub_left, mul_left - 1, div_left))

        # 나눗셈 연산자를 사용할 수 있는 경우
        if 0 < div_left:
            stack.append((path + ['/'], add_left, sub_left, mul_left, div_left - 1))
    
    return operator_combinations


n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

operator_combinations = Make_Operator_Combinations(operators[0], operators[1], operators[2], operators[3])

# print(len(operator_combinations))
# for ops in operator_combinations:
#     print(ops)

max_result = -int(1e9)
min_result = int(1e9)

# 연산자 조합의 수만큼 계산
for operator in operator_combinations:
    result = numbers[0]
    if ['-', '/', '+', '+', '*'] == operator:
        a = 0
    for i in range(1,n): 
        if '+' == operator[i-1]:
            result += numbers[i]
        elif '-' == operator[i-1]:
            result -= numbers[i]
        elif '*' == operator[i-1]:
            result *= numbers[i]
        elif '/' == operator[i-1]:
            if 0 > result:
                result = -(-result // numbers[i])
            else:
                result //= numbers[i]
    
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)


