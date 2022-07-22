class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = collections.defaultdict(list)
        
        visited = set()
        # Create graph
        for source, sink, weight in times:
            graph[source].append((sink,weight))
            
        # Min heap of (cost of node, node)
        heap = [(0,k)]
        time = 0
        # BFS
        while heap:
            curCost, curNode = heapq.heappop(heap)
            # Visited
            if curNode in visited: 
                continue
            # Want longest shortest path
            time = max(time, curCost)
            visited.add(curNode)
            for nei, neiCost in graph[curNode]:
                if nei not in visited:
                    heapq.heappush(heap, (curCost+neiCost, nei))
        # BFS would traverse all nodes if connected    
        return time if len(visited) == n else -1
                
                
                
