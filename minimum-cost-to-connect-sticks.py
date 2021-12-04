class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        heap = []
        count = 0
        
        for s in sticks:
            
            heapq.heappush(heap, s)
            
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
​
            count += (x+y)
            
            heapq.heappush(heap, x+y)
            
        return count
        
