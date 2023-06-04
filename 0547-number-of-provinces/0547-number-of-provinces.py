class UF:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False # already unioned
        else:
            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
                self.rank[p1] += self.rank[p2]
            else:
                self.par[p1] = p2
                self.rank[p2] += self.rank[p1]
            return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UF(n)
        provinces = n
        # Union all connected cities to find out how many provines
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] and uf.union(i, j):
                    provinces -= 1
        return provinces
        
        