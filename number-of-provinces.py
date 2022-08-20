class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1 for _ in range(n)] # To union onto larger rank
        
        def find(n):
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # Need to union disjointed sets
            if p1 != p2:
                if rank[p1] > rank[p2]:
                    par[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    par[p1] = p2
                    rank[p2] += rank[p1]
        
        for i in range(n):
            for j in range(n):
                # Ignore same nodes
                if i != j and isConnected[i][j] == 1:
                    union(i, j)
        count = 0
