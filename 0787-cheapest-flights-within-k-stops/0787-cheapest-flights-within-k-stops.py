class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = collections.defaultdict(list) # (from: [(cost, to)])
        
        for start, end, cost in flights:
            graph[start].append((cost, end))
            
        heap = [(0, src, k)] # (cost, stop, kLeft)
        visited = set()
        
        while heap:
            cost, stop, kLeft = heapq.heappop(heap)
            if stop == dst:
                return cost
            if (stop, kLeft) in visited:
                continue
            visited.add((stop, kLeft))
            if kLeft >= 0:
                for neiCost, nei in graph[stop]:
                    if (nei, kLeft-1) not in visited:
                        heapq.heappush(heap, (cost+neiCost, nei, kLeft-1))
        return -1
                
            
        
        