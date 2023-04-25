class SmallestInfiniteSet:

    def __init__(self):
        self.nums = set()
        self.heap = []
        for n in range(1, 1001):
            heapq.heappush(self.heap, n)
            self.nums.add(n)
        

    def popSmallest(self) -> int:
        res = -1
        res = heapq.heappop(self.heap)
        while res not in self.nums:
            res = heapq.heappop(self.heap)
        self.nums.remove(res)
        return res
        

    def addBack(self, num: int) -> None:
        self.nums.add(num)
        heapq.heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)