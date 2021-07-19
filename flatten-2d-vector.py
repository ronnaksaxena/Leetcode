class Vector2D:
​
    def __init__(self, vec: List[List[int]]):
        self.arr = []
        for elem in vec:
            for i in elem:
                self.arr.append(i)
        self.idx = 0
​
    def next(self) -> int:
        self.idx += 1
        return self.arr[self.idx-1]
​
    def hasNext(self) -> bool:
        return self.idx < len(self.arr)
​
​
# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
