class Logger:
​
    def __init__(self):
        self.timeStamps = {}
        
​
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.timeStamps:
            self.timeStamps[message] = timestamp
            return True
        elif timestamp >= (self.timeStamps[message] + 10):
            self.timeStamps[message] = timestamp
            return True
        else:
            return False #new timestamps <= message's timestamp + 10
        
​
​
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
​
'''
