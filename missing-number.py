class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        elems = set(nums)
        
        for i in range(len(nums)):
            if i not in elems:
                return i
            
        return len(nums)
