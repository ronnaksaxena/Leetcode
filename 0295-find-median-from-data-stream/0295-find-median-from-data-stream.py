import heapq
class MedianFinder:
    '''
    maxH
    -1
    1
    2
    
    
    minH
    3
    5
    addNum algo:
    1. Add to respective heap if val <= maxH[-1]: push -> maxH
        else push -> minH
    2. maintain order of heap if abs(len(maxH) - len(minH)) >= 2
    if maxH length > minH length: pop from maxH and push to minH
    else pop from minH and push to minH
    
    worst case time O(logN), space O(N)
    
    finMedian algo:
    if len(maxH) == len(minH):
        return (maxH[-1] + minH[-1]) / 2
    else:
        return top of whichever heap is longer
    time: O(1)
    '''

    def __init__(self):
        self.minH = []
        self.maxH = []

    def addNum(self, num: int) -> None:
        # CAREFUL of negative values for max heap
        # Add to respective heap
        if self.maxH and num <= -self.maxH[0]:
            heapq.heappush(self.maxH, -num) # negative to maintain max heap
        else:
            heapq.heappush(self.minH, num)
        # Maintain heaps structure
        if abs(len(self.minH) - len(self.maxH)) >= 2:
            # Max Heap is longer
            if len(self.maxH) > len(self.minH):
                heapq.heappush(self.minH, -heapq.heappop(self.maxH))
            # Min Heap is longer
            else:
                heapq.heappush(self.maxH, -heapq.heappop(self.minH))
        return
            
        

    def findMedian(self) -> float:
        # CAREFUL of negative values for max heap
        # Even number of values so take median
        if len(self.minH) == len(self.maxH):
            return (self.minH[0] + (-1 *self.maxH[0])) / 2
        # Odd number of values so take middle element
        else:
            return self.minH[0] if len(self.minH) > len(self.maxH) else (-1 *self.maxH[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()