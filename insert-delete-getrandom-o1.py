class RandomizedSet:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = {}
​
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if not val in self.dict:
            self.list.append(val)
            self.dict[val] = len(self.list)-1
            return True
        return False
​
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            valIdx = self.dict[val]
            lastElem = self.list[-1]
            self.list[valIdx], self.dict[lastElem] = lastElem, valIdx
            self.list.pop()
            self.dict.pop(val)
            return True
        return False
​
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.list[randint(0,len(self.list)-1)]
        
​
​
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
