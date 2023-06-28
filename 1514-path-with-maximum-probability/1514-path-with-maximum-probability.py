class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = collections.defaultdict(list)
        
        for prob, (n1, n2) in zip(succProb, edges):
            graph[n1].append((n2, prob))
            graph[n2].append((n1, prob))
        
        heap = [(-1, start)] # prob, node
        visited = set()
        
        while heap:
            curCost, node = heapq.heappop(heap)
            curCost *= -1
            
            if node == end:
                return curCost
            if node in visited:
                continue
            visited.add(node)
            
            
            for nei, prob in graph[node]:
                if nei not in visited:
                    heapq.heappush(heap, (-(curCost * prob), nei))
        return 0
            
            
        
        