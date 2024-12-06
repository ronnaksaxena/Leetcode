class UF:
    def __init__(self, n):
        self.rank = [0 for _ in range(n)]
        self.par = [i for i in range(n)]
        self.components = n

    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def isConnected(self, n1, n2):
        return self.find(n1) == self.find(n2)

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
                self.rank[p1] += 1
            else:
                self.par[p1] = p2
                self.rank[p2] += 1
            self.components -= 1

    def isAllConnected(self):
        return self.components == 1



class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UF(n)

        heap = []
        for t, person1, person2 in logs:
            heapq.heappush(heap, (t, person1, person2))

        while heap:
            time, person1, person2 = heapq.heappop(heap)
            if not uf.isConnected(person1, person2):
                uf.union(person1, person2)
                if uf.isAllConnected():
                    return time

        return -1


        