class MedianFinder:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small, self.large = [], [] #max heap, min heap
​
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1*num)
        
        if self.small and self.large and (self.small[0]*-1) > self.large[0]:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))
            
        if len(self.small) > len(self.large) +1:
            heapq.heappush(self.large, (-1 * heapq.heappop(self.small)))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, (-1 * heapq.heappop(self.large)))
​
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return ((self.small[0] * -1 )+ self.large[0]) / 2
        
​
​
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
