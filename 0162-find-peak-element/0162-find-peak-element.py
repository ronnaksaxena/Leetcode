class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + (r-l)//2)
            peak = nums[m]
            left = nums[m-1] if (m-1) >= 0 else float('-inf')
            right = nums[m+1] if (m+1) < len(nums) else float('-inf')
            if left < peak > right:
                return m
            if left < peak < right:
                l = m + 1
            else:
                r = m -1

        return -1

        