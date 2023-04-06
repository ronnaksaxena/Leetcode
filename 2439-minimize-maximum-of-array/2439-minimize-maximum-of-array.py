class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        pre = 0
        answer = float('-inf')
        
        for i in range(len(nums)):
            pre += nums[i]
            answer = max(answer, math.ceil(pre/(i+1)))
            
        return answer