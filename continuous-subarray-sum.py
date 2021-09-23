class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        acc = 0
        map = {0 : -1}
        
        for i in range(len(nums)):
            
            acc += nums[i]
            if k:
                acc %= k
            
            if acc in map:
                if i - map[acc] >= 2:
                    return True
            else: map[acc] = i
            
        return False
        
