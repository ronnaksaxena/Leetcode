class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            k = nums[:i]+nums[i+1:]
            if k==sorted(k) and len(k)==len(set(k)):
                return True
        return False
