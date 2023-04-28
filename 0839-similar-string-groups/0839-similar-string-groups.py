class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        else:
            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
                self.rank[p1] += self.rank[p2]
            else:
                self.par[p1] = p2
                self.rank[p2] += self.rank[p1]
            return True

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(s1, s2):
            dif = 0
            for a, b in zip(s1, s2):
                if a != b:
                    dif += 1
            return dif == 0 or dif == 2
        n = len(strs)
        uf = UnionFind(n)
        count = n
        for i in range(n):
            for j in range(i+1, n):
                if isSimilar(strs[i], strs[j]) and uf.union(i,j):
                    count -= 1
                
        return count
                
        