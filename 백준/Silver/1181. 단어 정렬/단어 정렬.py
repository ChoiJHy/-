def MergeSort(arr):

    if len(arr) <= 1:
        return arr
    
    # 리스트의 길이가 2인경우는 나누지 않고 바로 정렬해서 리턴
    # if len(arr) == 2:
    #     return [arr[0], arr[1]] if len(arr[0]) < len(arr[1]) else [arr[1], arr[0]]
    
    # 리스트를 절반으로 나눈다.
    middle = len(arr) // 2
    left_arr = MergeSort(arr[:middle]) # 0부터 middle 이전까지
    right_arr = MergeSort(arr[middle:]) # middle부터 마지막 인덱스까지 

    return Merge(left_arr, right_arr)

def Merge(left, right):
    result = []
    i = j = 0

    # # 오름차순으로 정렬하면서 병합을 진행한다.
    # while i < len(left) and j < len(right):
    #     if len(left[i]) < len(right[j]):
    #         if not result or result[-1] != left[i]: # 리스트가 비어있거나 맨 마지막 들어간 요소와 중복이 아닐 때
    #             result.append(left[i])
    #         i += 1
    #     elif len(left[i]) > len(right[j]):
    #         if not result or result[-1] != right[j]:
    #             result.append(right[j])
    #         j += 1
    #     else: # 길이가 같다면 사전순으로 정렬하고 중복을 확인한다.
    #         if left[i] < right[j]:
    #             if not result or result[-1] != left[i]:
    #                 result.append(left[i])
    #             i += 1
    #         elif left[i] > right[j]:
    #             if not result or result[-1] != right[j]:
    #                 result.append(right[j])
    #             j += 1
    #         else: # 중복된 단어라면 한 번만 추가한다.
    #             if not result or result[-1] != left[i]:
    #                 result.append(left[i])
    #             i += 1
    #             j += 1

     # 두 리스트를 비교하며 하나로 합친다.
    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]) or (len(left[i]) == len(right[j]) and left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 리스트에 남아있는 요소들 추가
    # while i < len(left):
    #     if not result or result[-1] != left[i]:
    #         result.append(left[i])
    #     i += 1
    
    # while j < len(right):
    #     if not result or result[-1] != right[j]:
    #         result.append(right[j])
    #     j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    
    return result


def IsLowerAlpha(word):

    if len(word) == 0:
        return False
    for char in word:
        if not ('a' <= char <= 'z'):
            return False
    
    return True


# 단어 갯수 입력
n = int(input())
words = set()
# words = [input() for _ in range(n)] # n개의 단어 입력
# words = []

for _ in range(n):
    words.add(input().strip())

# for _ in range(n):
#     words.append(input())
#     # if IsLowerAlpha(word):
#     #     words.append(word)
    

sorted_list = MergeSort(list(words))

for word in sorted_list:
    print(word)
