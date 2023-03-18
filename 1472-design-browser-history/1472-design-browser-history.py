class BrowserHistory:
    def __init__(self, homepage: str):
        
        self.backward = [] # stack
        self.foreward = [] # stack
        self.curUrl = homepage
        

    def visit(self, url: str) -> None:
        self.foreward.clear()
        self.backward.append(self.curUrl)
        self.curUrl = url
        return

    def back(self, steps: int) -> str:
        for _ in range(steps):
            # Too many steps
            if not self.backward:
                break
            self.foreward.append(self.curUrl)
            self.curUrl = self.backward.pop()
        return self.curUrl
            
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.foreward:
                break
            self.backward.append(self.curUrl)
            self.curUrl = self.foreward.pop()
            
        return self.curUrl
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)