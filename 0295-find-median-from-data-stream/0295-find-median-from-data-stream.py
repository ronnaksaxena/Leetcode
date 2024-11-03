'''
1 2 3 4 7 5 6

divide data into 2 heaps

lowerHalf in maxHeap     upperHalf in minHeap

       1 2                        3 4 7
'''


class MedianFinder:

    def __init__(self):
        self.lowerHalf = [] # maxHeap
        self.upperHalf = [] # minHeap
        

    def addNum(self, num: int) -> None:
        '''
        if not upperHalf or num >= top of upperHalf add to upper
        else: push to lowerHalf

        if lengths of heap differ by 2: pop from larger heap and push onto smaller heap
        '''
        if not self.upperHalf or num >= self.upperHalf[0]:
            heapq.heappush(self.upperHalf, num)
        else:
            heapq.heappush(self.lowerHalf, -num)

        if abs(len(self.upperHalf) - len(self.lowerHalf)) == 2:
            if len(self.upperHalf) > len(self.lowerHalf):
                heapq.heappush(self.lowerHalf, -heapq.heappop(self.upperHalf))
            else:
                heapq.heappush(self.upperHalf, -heapq.heappop(self.lowerHalf))
        

    def findMedian(self) -> float:
        '''
        the top of whichever has more elements is median
        else avg of top of 2
        '''
        if len(self.upperHalf) == len(self.lowerHalf):
            return (-self.lowerHalf[0] + self.upperHalf[0]) / 2
        else:
            return self.upperHalf[0] if len(self.upperHalf) > len(self.lowerHalf) else -self.lowerHalf[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()