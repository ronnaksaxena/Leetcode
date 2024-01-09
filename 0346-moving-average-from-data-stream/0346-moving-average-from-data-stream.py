class MovingAverage:

    def __init__(self, size: int):
        self.q = collections.deque()
        self.runningSum = 0
        self.size = size
        

    def next(self, val: int) -> float:
        '''
        - add val to q
        - runningSum += val
        - if lenght of q > size:
            oldVal deque
            runningSum -= oldVal
        - return runningSum / len(q)
        
        Time: O(1)
        Space: O(n)
        '''
        self.q.append(val)
        self.runningSum += val
        if len(self.q) > self.size:
            oldVal = self.q.popleft()
            self.runningSum -= oldVal
        return self.runningSum / len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)