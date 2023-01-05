class Union:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(self.n)]
        self.rank = [1 for _ in range(self.n)]
    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.par[p1] = p2
            else:
                self.par[p2] = p1
                self.rank[p1] += 1
    def isConnected(self, n1, n2):
        return self.find(n1) == self.find(n2)
# Edges between points
class Edge:
    def __init__(self, v1, v2, cost):
        self.v1 = v1
        self.v2 = v2
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost
        
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        # Construct all edge combinations between points
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edge = Edge(i, j, cost)
                heapq.heappush(heap, edge)
                
        edgesRemaining = len(points) - 1
        union = Union(len(points))
        cost = 0
        
        while heap and edgesRemaining > 0:
            curEdge = heapq.heappop(heap)
            
            if not union.isConnected(curEdge.v1, curEdge.v2):
                union.union(curEdge.v1, curEdge.v2)
                edgesRemaining -= 1
                cost += curEdge.cost
                
        return cost

        