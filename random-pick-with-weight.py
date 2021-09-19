class Solution:
​
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum
​
    def pickIndex(self) -> int:
        ran = random.randint(1,self.total_sum)
        l, r = 0, len(self.prefix_sums)
        while l < r:
            mid = l + (r-l)//2
            
            if self.prefix_sums[mid] < ran:
                l = mid + 1
            else:
                r = mid
                
        return l
        
​
​
# Your Solution object will be instantiated and called as such:
