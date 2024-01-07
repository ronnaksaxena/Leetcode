class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        ran = random.randint(1,self.total_sum) # First p sum has to be >= 1
        # right boundary is highestSum
        l, r = 0, len(self.prefix_sums)
        while l < r:
            m = l + (r-l) // 2
            if self.prefix_sums[m] < ran:
                l = m + 1
            else:
                r = m
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()