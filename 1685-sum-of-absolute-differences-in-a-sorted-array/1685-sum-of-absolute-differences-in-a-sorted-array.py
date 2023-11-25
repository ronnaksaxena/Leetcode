class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre = [0 for _ in range(len(nums))]
        runningSum = 0
        for i,n in enumerate(nums):
            runningSum += n
            pre[i] = runningSum
        ans = [0] * len(nums)
        for i in range(len(nums)):
            left = pre[i-1] if i > 0 else 0
            right = pre[-1] - pre[i]
            ans[i] = (nums[i]*i-left) + (right - nums[i] * (len(nums)-1-i))
        return ans
            
            
        