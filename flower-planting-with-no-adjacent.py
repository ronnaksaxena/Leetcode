class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph=defaultdict(set)
        for u,v in paths:
            graph[u].add(v)
            graph[v].add(u)
            
        res=[0]*(n+1)
        for i in range(1, n+1):
            # check connected neighbors' color
            available={1,2,3,4}
            for n in graph[i]:
                if res[n] in available:
                    available.remove(res[n])            
            res[i]=available.pop()
        return res[1:]
