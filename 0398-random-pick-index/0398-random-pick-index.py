class Solution:

    def __init__(self, nums: List[int]):
        self.indices = collections.defaultdict(list)
        for i, n in enumerate(nums):
            self.indices[n].append(i)
        

    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)