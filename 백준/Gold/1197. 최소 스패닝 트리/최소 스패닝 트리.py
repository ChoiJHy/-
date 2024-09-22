import sys
input = sys.stdin.readline

#크루스칼 알고리즘으로 풀어내기 위해 가져왔다.
class UnionFind:
    def __init__(self, size):
        # 각 노드는 자기 자신을 부모로 설정하고, 랭크는 1로 초기화
        self.parent = list(range(size))
        self.rank = [1] * size

    def Find(self, x):
        # 경로 압축을 적용하여 루트를 찾음
        if self.parent[x] != x:
            self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]

    def Union(self, x, y):
        # 두 집합을 합치는 연산, 랭크 기반으로 결합
        rootX = self.Find(x)
        rootY = self.Find(y)

        if rootX != rootY:
            # 랭크에 따라 더 작은 트리를 큰 트리에 붙임
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def Kruskal_Algorithm(vertices, edges):
    # 간선들을 가중치 순으로 정렬 (오름차순)
    edges.sort(key = lambda edge: edge[2])

    # 유니온 파인드 초기화
    uf = UnionFind(vertices)

    total_weight = 0
    # 간선을 하나씩 확인하면서 MST를 구성
    for edge in edges:
        u, v, weight = edge # 간선을 이루는 두 정점과 가중치
        # u와 v가 같은 집합이 아니라면 사이클이 발생하지 않으므로 선택한다.
        if uf.Find(u) != uf.Find(v):
            uf.Union(u, v)
            total_weight += weight
    
    return total_weight

v, e = map(int, input().split())

edges = []
for _ in range(e):
    edges.append(list(map(int, input().split())))

print(Kruskal_Algorithm(v + 1, edges))