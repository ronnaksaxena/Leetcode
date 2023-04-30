class DSU:
    def __init__(self, N):
        self.parents = defaultdict(lambda: None)
        self.sizes = defaultdict(int)
        self.components = N
        
    def find(self, a):
        if a not in self.parents:
            self.parents[a] = a
            self.sizes[a] = 1
            return a

        root = a
        while self.parents[root] != root:
            root = self.parents[root]

        while self.parents[a] != a:
            nxt = self.parents[a]
            self.parents[a] = root
            a = nxt

        return root

    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)

        if roota == rootb:
            return False

        self.components -= 1
        
        if self.sizes[roota] > self.sizes[rootb]:
            self.sizes[roota] += self.sizes[rootb]
            self.sizes[rootb] = 0
            self.parents[rootb] = roota
        else:
            self.sizes[rootb] += self.sizes[roota]
            self.sizes[roota] = 0
            self.parents[roota] = rootb
        return True
    
    def is_one_component(self):
        return self.components == 1

class Solution:
    def maxNumEdgesToRemove(self, N: int, edges: List[List[int]]) -> int:
        E = len(edges)
        edges.sort(key = lambda x: -x[0])
        
        a, b = DSU(N), DSU(N)
        
        used = 0
        for t,u,v in edges:
            if t == 3: # alice + bob
                if a.find(u) != a.find(v):
                    used += a.union(u, v)
                    b.union(u, v)
            if t == 1: # alice
                if a.find(u) != a.find(v):
                    used += a.union(u, v)
            if t == 2: # bob
                if b.find(u) != b.find(v):
                    used += b.union(u, v)

        if not a.is_one_component() or not b.is_one_component():
            return -1
        
        return E - used