import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size # 초기 랭크는 모두 1


    def Find(self, x):
        # 루트를 찾는 과정에서 경로 압축을 적용
        if self.parent[x] != x:
            self.parent[x] = self.Find(self.parent[x])  # 경로 압축
        return self.parent[x]

    def Union(self, a, b):
        # 두 원소가 속한 집합을 합칩니다.
        root_a = self.Find(a)
        root_b = self.Find(b)

        if root_a != root_b:
            # 랭크 기반으로 트리의 높이가 낮은 쪽을 높은 쪽에 연결
            if self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            elif self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            else:
                # 랭크가 같다면 한쪽 트리의 높이를 증가시키며 합침
                self.parent[root_b] = root_a
                self.rank[root_a] += 1  

n, m = map(int, input().split())

uf = UnionFind(n + 1)
component_check = [False] * (n + 1)

for _ in range(m):
    start, end = map(int, input().split())
    uf.Union(start, end)

component_count = 0

# for i in range(1, n + 1):
#     component = uf.Find(i)

for i in range(1, n + 1):
    component = uf.Find(i)
    if False == component_check[component]:
        component_check[component] = True
        component_count += 1

print(component_count)