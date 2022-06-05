import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: #edge case
            return stones[0]
        heap = []
        
        for s in stones: 
            heapq.heappush(heap, -s) #negative so its a max heap
            
        while len(heap) > 1:
            #get the two largest elems and smash together
            val1 = (-1 * heapq.heappop(heap))
            val2 = (-1 * heapq.heappop(heap))
            smashed = abs(val1-val2)
            print(smashed, val1, val2)
            if smashed != 0: #not the same value
                heapq.heappush(heap, -smashed)
                
        return -1 * heap[0] if heap else 0
        
        
        
        '''
        max heap
        [2,7,4,1,8,1]
        7, 8
        smashed val = abs(8-7)
        if != 0 push to heap
        
        until len of heap is 1
        
        
        '''
