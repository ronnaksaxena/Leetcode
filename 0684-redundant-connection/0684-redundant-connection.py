class UF:
    def __init__(self, n):
        self.par = {i: i for i in range(1, n+1)}
        self.rank = {i:1 for i in range(1, n+1)}

    def find(self, node):
        while node != self.par[node]:
            # Compression
            self.par[node] = self.par[self.par[node]]
            # Find root
            node = self.par[node]
        return node

    # Returns True if already unioned
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return True
        else:
            if self.rank[p1] > self.rank[p2]:
                self.rank[p1] += 1
                self.par[p2] = p1
            else:
                # n2 parent is ranked higher
                self.rank[p2] += 1
                self.par[p1] = p2

            return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # We know there is exactle 1 extra edge so n is len(edges)
        n = len(edges)
        uf = UF(n)

        for a, b in edges:
            if not uf.union(a,b):
                continue
            else:
                res = [a,b]
        return res
        