import sys

def up_heapify(heap, index):
    child_index = index
    while child_index != 0:
        parent_index = (child_index - 1) // 2
        if heap[parent_index] < heap[child_index]:
            heap[parent_index], heap[child_index] = heap[child_index], heap[parent_index]
            child_index = parent_index
        else:
            return

# 삭제를 위한 과정 
# 루트노드를 삭제하고 마지막 원소를 루트로 이동
# 큰 값을 가진 자식과 위치를 교환
# 교환한 노드에서 다시 큰 값을 가진 자식과 위치를 교환
# 위 과정을 반복 
def down_heapify(heap, index, heap_size):
    # 1. 부모노드와 자식노드들의 인덱스 지정
    parent = index
    left_child = 2 * parent + 1
    right_child = 2 * parent + 2

    # 2. 왼쪽 자식노드, 오른쪽 자식노드 중 가장 큰 노드를 선택
    if left_child < heap_size and heap[left_child] > heap[parent]:
        parent = left_child
    if right_child < heap_size and heap[right_child] > heap[parent]:
        parent = right_child

    # 3. 자식노드중 가장 큰 노드와 부모노드를 바꿈 (배열의 값 교환)
    if parent != index:
        heap[parent], heap[index] = heap[index], heap[parent]
     # 4. 바뀐 자식노드의 힙을 재 구조화
        down_heapify(heap, parent, heap_size)

def MaxHeapInsert(heap, n):
    heap.append(n)
    up_heapify(heap, len(heap) - 1)

def MaxHeapPop(heap):
    result = 0
    if heap:
        heap[0], heap[len(heap) - 1] =  heap[len(heap) - 1], heap[0]
        result = heap.pop()
        down_heapify(heap, 0, len(heap))

    return result

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        MaxHeapInsert(heap, x)
    else:
        sys.stdout.write(str(MaxHeapPop(heap)) + '\n')