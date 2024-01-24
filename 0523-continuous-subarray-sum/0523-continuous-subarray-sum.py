class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        pre = {0:-1}
        
        runningSum = 0
        for i, n in enumerate(nums):
            runningSum += n
            runningSum %= k
            if (runningSum) in pre:
                if i - pre[(runningSum)] >= 2:
                    return True
            else:
                pre[runningSum] = i
        
        return False
        