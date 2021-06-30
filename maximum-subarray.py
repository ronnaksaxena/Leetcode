class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMaxSum, totalMaxSum = nums[0], nums[0]
        for num in nums[1:]:
            curMaxSum = max(num, curMaxSum + num)
            totalMaxSum = max(totalMaxSum, curMaxSum)
            
        return totalMaxSum
        
