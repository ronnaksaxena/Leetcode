class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        visited = set()
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(cur, prev):
            # Loop was detected
            if cur in visited:
                return False
            
            visited.add(cur)
            
            # Traverse all neighbors that were not the previous node
            for u in graph[cur]:
                # Avoid going backwards
                if u == prev:
                    continue
                # Continue search and also stop if cycle was detected
                if not dfs(u, cur):
                    return False
            # No cycle was detected
            return True
        
        # No cycle was detected and every node was visited
        return dfs(0,-1) and len(visited) == n
                
        
