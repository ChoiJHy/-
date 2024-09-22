import sys
input = sys.stdin.readline
#recursion error 방지
sys.setrecursionlimit(10**6)

arr = []

while True:
    try:
        arr.append(int(input()))
    except:
        break

def solution(array):
    if 0 == len(array):
        return
    
    left_arr, right_arr = [], []
    mid = array[0]

    # 배열을 순회하며 root보다 커지는 부분을 기점으로 left, right 배열로 나눈다.
    for i in range(1, len(array)):
        if array[i] > mid:
            left_arr = array[1:i]
            right_arr = array[i:]
            break
    else:
        #모두 mid보다 작은 경우
        left_arr = array[1:]
    
    solution(left_arr)
    solution(right_arr)
    print(mid)

solution(arr)