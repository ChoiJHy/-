def merge_sort(words):
    if len(words) <= 1:
        return words

    # 중간 지점 설정
    mid = len(words) // 2
    left = merge_sort(words[:mid])  # 왼쪽 반 정렬
    right = merge_sort(words[mid:])  # 오른쪽 반 정렬

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # 두 리스트를 비교하며 하나로 합친다.
    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]) or (len(left[i]) == len(right[j]) and left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남아 있는 원소를 추가
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# 입력 받기
n = int(input())
words = set()  # 중복을 제거하기 위해 set 사용

for _ in range(n):
    words.add(input().strip())

# 리스트로 변환 후 병합 정렬 호출
sorted_words = merge_sort(list(words))

# 출력
for word in sorted_words:
    print(word)