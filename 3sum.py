class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = []
        nums.sort()
        for i in range(0, len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                self.helper(i,nums,ans)
        return ans
    
    def helper(self, cur, nums, ans):
        lo, hi = cur+1, len(nums)-1
        while lo<hi:
            val = nums[cur]+nums[lo]+nums[hi]
            if val < 0:
                lo += 1
            elif val > 0:
                hi -= 1
            else:
                ans.append([nums[cur],nums[lo],nums[hi]])
                lo += 1
                hi -= 1
                while lo<hi and nums[lo]==nums[lo-1]:
                    lo += 1
        
