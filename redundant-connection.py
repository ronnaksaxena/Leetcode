class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(set)
        
        def dfs(source, target, seen):
            if source not in seen:
                seen.add(source)
                # source connects to target
                if source == target:
                    return True
                
                return any(dfs(u,target,seen) for u in graph[source])
        
        for source, sink in edges:
            seen = set()
            if source in graph and sink in graph and dfs(source, sink, seen):
                return [source,sink]
            graph[source].add(sink)
            graph[sink].add(source)
        
        
