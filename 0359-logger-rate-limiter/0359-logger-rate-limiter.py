class Logger:

    def __init__(self):
        self.q = collections.deque() # (timestamp, msg)
        self.msg = set()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        while self.q:
            t, m = self.q[0]
            if t > (timestamp - 10):
                break
            self.q.popleft()
            self.msg.remove(m)

        if message in self.msg:
            return False
        else:
            self.q.append((timestamp, message))
            self.msg.add(message)
            return True


        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)