class MinStack:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minData = []
​
    def push(self, val: int) -> None:
        if not self.data:
            self.data.append(val)
            self.minData.append(val)
            return
        self.data.append(val)
        self.minData.append(min(self.minData[-1], val))
        return
​
    def pop(self) -> None:
        self.minData.pop()
        return self.data.pop()
        
​
    def top(self) -> int:
        return self.data[-1]
        
​
    def getMin(self) -> int:
        return self.minData[-1]
        
​
