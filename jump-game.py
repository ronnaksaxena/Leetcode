class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        lastGoodIdx = len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= lastGoodIdx:
                lastGoodIdx = i
        
        return lastGoodIdx == 0
