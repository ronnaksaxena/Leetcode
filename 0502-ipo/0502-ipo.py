class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        heap = []
        ptr = 0
        
        for _ in range(k):
            while ptr < len(projects) and projects[ptr][0] <= w:
                heapq.heappush(heap, -projects[ptr][1])
                ptr += 1
            if not heap:
                break
            w += -heapq.heappop(heap)
        return w
            
            
            
            
        