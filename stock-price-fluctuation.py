import heapq
class StockPrice:
​
    def __init__(self):
        self.timeStamps = {} # {timestamps : price}
        self.curPrice = [] #[MaxTimeStamp, price]
        self.maxPrices = []
        self.minPrices = []
​
    def update(self, timestamp: int, price: int) -> None:
        '''
        make sure our map is updated
        '''
        self.timeStamps[timestamp] = price
        # update curPrice if needed
        if not self.curPrice or self.curPrice[0] <= timestamp:
            self.curPrice = [timestamp, price]
        #update heaps
        heapq.heappush(self.maxPrices, (-price,timestamp))
        heapq.heappush(self.minPrices, (price,timestamp))
            
​
    def current(self) -> int:
        return self.curPrice[1]
​
    def maximum(self) -> int:
        '''
        update max heap and return top
        '''
        # pop all non updated tops
        while self.maxPrices and (self.maxPrices[0][0] *-1) != self.timeStamps[self.maxPrices[0][1]]:
            heapq.heappop(self.maxPrices)
        return self.maxPrices[0][0] * -1
        
​
    def minimum(self) -> int:
        '''
        update max heap and return top
        '''
        while self.minPrices and self.minPrices[0][0] != self.timeStamps[self.minPrices[0][1]]:
            heapq.heappop(self.minPrices)
        return self.minPrices[0][0]
​
​
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
