class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
​
        ans = [1 for _ in range(len(nums))]
        
        for i in range(1,len(nums)):
            ans[i] = nums[i-1] * ans[i-1]
        
        acc = 1
        
        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i] * acc
            acc *= nums[i]
        
        return ans
