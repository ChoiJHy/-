import sys
# 병합정렬을 사용하여 문제해결 
def MergeSort(arr):

    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left_arr = MergeSort(arr[:middle])
    right_arr = MergeSort(arr[middle:])

    return Merge(left_arr, right_arr)

def Merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # 작은 수를 넣어주고 인덱스를 올린다.
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
        else: # 만약 두 수가 같다면 하나만 넣고 양쪽의 인덱스를 올려준다.(중복 무시)
            result.append(left[i])
            i += 1
            j += 1

    # 아직 남아있는 요소들을 넣어준다.
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

sorted_arr = MergeSort(arr)

for i in range(len(sorted_arr)):
    sys.stdout.write(str(sorted_arr[i]) + '\n')