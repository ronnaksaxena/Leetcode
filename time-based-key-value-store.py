class TimeMap:
​
    def __init__(self):
        # {key: [(timeStamps, value)]}
        self.stamps = collections.defaultdict(list)
        
​
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stamps[key].append((timestamp, value))
​
    def get(self, key: str, timestamp: int) -> str:
        # key doesn't exists
        if key not in self.stamps:
            return ''
        # find timeStamp that is <= timestamp arg from our list
        stamps = self.stamps[key]
        res = ''
        l, r = 0, len(stamps)-1
        while l <= r:
            m = l + (r-l) // 2
            # Potential candidate
            if stamps[m][0] <= timestamp:
                res = stamps[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
​
        
​
​
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
