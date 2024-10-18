class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if self.minHeap and num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                element = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -element)
            else:
                element = -heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, element)

        

    def findMedian(self) -> float:
        # print(f'minHeap {self.minHeap} maxHeap {self.maxHeap}')
        if len(self.minHeap) == len(self.maxHeap):
            return ((-self.maxHeap[0] + self.minHeap[0]) / 2)
        
        return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()