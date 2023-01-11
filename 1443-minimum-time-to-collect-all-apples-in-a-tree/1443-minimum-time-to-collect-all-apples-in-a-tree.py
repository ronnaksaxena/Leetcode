class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = collections.defaultdict(list)
        
        for par, child in edges:
            graph[par].append(child)
            graph[child].append(par)
        visited = set()
            
        def dfs(node, visited):
            if node in visited:
                return
            visited.add(node)
            applesFound = 0
            for child in graph[node]:
                if child not in visited:
                    applesFound += dfs(child, visited)
            
            if applesFound or hasApple[node]:
                return applesFound + 2
            
            return applesFound
        answer = dfs(0, visited) -2
        
        return answer if answer > 0 else 0
            
        
        
                
        