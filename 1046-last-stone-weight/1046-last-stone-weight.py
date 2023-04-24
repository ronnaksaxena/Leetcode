class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) >= 2:
            y, x = -heapq.heappop(heap), -heapq.heappop(heap)
            if x == y:
                continue
            else:
                heapq.heappush(heap, -(y-x))
        
        return -heap[0] if heap else 0
                
        