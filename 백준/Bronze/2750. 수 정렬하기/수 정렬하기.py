import sys

def QuickSort(arr, left, right):
    # left ~ right를 in place 방식으로 퀵정렬

    point_left = left
    point_right = right
    pivot = arr[(left + right) // 2]

    while point_left <= point_right: # 양쪽에서 오던 포인터가 서로 교차할 때 까지
        while arr[point_left] < pivot: point_left += 1 # 왼쪽에 있는 값들중 피벗보다 큰 값이 나올 때 까지
        while arr[point_right] > pivot: point_right -= 1 # 오른쪽에 있는 값들중 피벗보다 작은 값이 나올 때 까지

        if point_left <= point_right: # 포인터의 위치가 교차하지 않았다면 
            arr[point_left], arr[point_right] = arr[point_right], arr[point_left] # 포인터에 있는 값의 위치를 서로 바꿈
            # 포인터 이동 
            point_left += 1
            point_right -= 1

    # 오른쪽에서 오던 커서가 왼쪽에 도달할 때 까지
    if left < point_right: QuickSort(arr, left, point_right)
    # 왼쪽에서 오던 커서가 오른쪽에 도달할 때 까지
    if point_left < right: QuickSort(arr, point_left, right)

# 입력
n = int(sys.stdin.readline())  # 수의 개수
number_list = [int(sys.stdin.readline()) for _ in range(n)]

# 제자리 퀵 정렬 수행
QuickSort(number_list, 0, n - 1)

# 출력
for num in number_list:
    print(num)