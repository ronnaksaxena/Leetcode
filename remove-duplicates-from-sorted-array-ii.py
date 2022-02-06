class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        i = 2
        
        for j in range(2, len(nums)):
            if nums[i-2] != nums[j]:
                nums[i] = nums[j]
                i += 1
                
        return i
                
        
        '''
        1   1   2   2   3   3
                        i
        
                            j
        if nums[j] >= nums[i]
        if i < 1 or (nums[i-2] != nums[j])
        
        final answer i+1
        
        
