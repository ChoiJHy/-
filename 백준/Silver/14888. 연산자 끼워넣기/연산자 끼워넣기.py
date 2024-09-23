import sys
input = sys.stdin.readline

def solution(add, sub, mul, div):
    i = 0 # numbers에 접근하기 위한 인덱스
    stack = [(numbers[0], add, sub, mul, div, i)] # 스택을 초기화함(path, 연산자들)
    max_result = -int(1e9)
    min_result = int(1e9)

    while stack:
        result, add_left, sub_left, mul_left, div_left, index = stack.pop()

        # 모든 연산자를 사용한 경우
        if 0 == add_left and 0 == sub_left and 0 == mul_left and 0 == div_left:
            max_result = max(max_result, result)
            min_result = min(min_result, result)
            continue

        # 덧셈 연산자를 사용할 수 있는 경우
        if 0 < add_left:
            stack.append((result + numbers[index+1], add_left - 1, sub_left, mul_left, div_left, index + 1))

        # 뺄샘 연산자를 사용할 수 있는 경우
        if 0 < sub_left:
            stack.append((result - numbers[index+1], add_left, sub_left - 1, mul_left, div_left, index + 1))
        
        # 곱셈 연산자를 사용할 수 있는 경우
        if 0 < mul_left:
            stack.append((result * numbers[index+1], add_left, sub_left, mul_left - 1, div_left, index + 1))

        # 나눗셈 연산자를 사용할 수 있는 경우
        if 0 < div_left:
            if 0 > result:
                stack.append((-(-result // numbers[index+1]), add_left, sub_left, mul_left, div_left - 1, index + 1))
            else:
                stack.append((result // numbers[index+1], add_left, sub_left, mul_left, div_left - 1, index + 1))

    print(max_result)
    print(min_result)
    
n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

solution(operators[0], operators[1], operators[2], operators[3])
