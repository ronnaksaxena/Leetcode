class HitCounter:
​
    def __init__(self):
        self.q = collections.deque()
​
    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)
        while self.q and (self.q[0] <= (timestamp-300)):
            self.q.popleft()
        
​
    def getHits(self, timestamp: int) -> int:
        while self.q and (self.q[0] <= (timestamp-300)):
            self.q.popleft()
        return len(self.q)
​
​
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
