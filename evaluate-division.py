class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adjList = collections.defaultdict(list)
        
        for i in range(len(equations)):
            dividend, divisor, val = equations[i][0], equations[i][1], values[i]
            adjList[dividend].append((divisor,val))
            adjList[divisor].append((dividend, (1/val)))
        
            
        ans = [0.0 for _ in range(len(queries))]
        
        for i in range(len(queries)):
            dividend, divisor = queries[i][0], queries[i][1]
            if not dividend in adjList or not divisor in adjList:
                ans[i] = -1.0
            elif dividend == divisor:
                ans[i] = 1.0
            else:
                visited = set()
                ans[i] = self.DFS(dividend, divisor, adjList, 1, visited)
        
        return ans
    
    def DFS(self, cur, target, adjList, product, visited):
        visited.add(cur)
        if cur==target:
            return product
        ret = -1.0
        
        for (u,val) in adjList[cur]:
            if not u in visited:
                ret = self.DFS(u, target, adjList, product*val, visited)
            if ret != -1.0:
                break
