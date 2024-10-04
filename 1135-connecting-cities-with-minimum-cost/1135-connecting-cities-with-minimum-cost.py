class UF:
    def __init__(self, n):
        self.par = {i: i for i in range(1, n+1)}
        self.rank = {i: 1 for i in range(1, n+1)}

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def isConnected(self, n1, n2):
        return self.find(n1) == self.find(n2)
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
    

class Edge:
    def __init__(self, v1, v2, cost):
        self.v1 = v1
        self.v2 = v2
        self.cost = cost
    
    def __lt__(self, other):
        return isinstance(other, Edge) and self.cost < other.cost
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        minHeap = []
        for v1, v2, cost in connections:
            heapq.heappush(minHeap, Edge(v1, v2, cost))

        visited = set()
        uf = UF(n)
        totalCost = 0
        while minHeap:
            e = heapq.heappop(minHeap)
            if not uf.isConnected(e.v1, e.v2):
                uf.union(e.v1, e.v2)
                totalCost += e.cost

        return totalCost if all(uf.isConnected(1, x) for x in range(1, n+1)) else -1

        