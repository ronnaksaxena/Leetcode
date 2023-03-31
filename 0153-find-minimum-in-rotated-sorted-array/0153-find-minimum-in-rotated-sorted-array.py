class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Time: O(logn)
        Space: O(1)
        
        '''
        # Needs to be len(nums) -1 because you're comparing to s[r]
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r-l)//2
            # Can't be pivot since this would mean its ascending
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[l]
                
        