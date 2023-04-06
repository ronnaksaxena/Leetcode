class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        par = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        
        def find(n):
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            else:
                if rank[p1] > rank[p2]:
                    par[p2] = p1
                elif rank[p1] < rank[p2]:
                    par[p1] = p2
                else:
                    par[p1] = p2
                    rank[p2] += 1
                return True
        
        # Check no redudant connections in edges
        for v1, v2 in edges:
            if not union(v1, v2):
                return False
        # Check all have same parent
        # Par array may not be updated yet so need to call find
        return all(find(x) == find(0) for x in range(n))