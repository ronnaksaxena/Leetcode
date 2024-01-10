class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        ouptut index
        
        - Garunteed peak element
        - No duplicates back to back
        - Non null input
        
        Brute Force: linear Scan O(N)
        [1,2,1,3,5,6,4]
           i
        check for peak element andn return index
        
        Optimize: BSearch O(logN)
        [1,2,3,4,3,1]
             m 3
        l           r
        if element is peak: return index
        if middle element is increasing: peak must be on right, incr L
        else middle element is decreasing: peak must be on left, dec R
        
        return -1 # No peak element
        
        '''
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r-l) // 2
            left = nums[m-1] if m > 0 else -inf
            right = nums[m+1] if m < len(nums) - 1 else -inf
            # Found peak?
            if left < nums[m] > right:
                return m
            # Increasing?
            elif left < nums[m] < right:
                l = m + 1
            # Decreasing
            else:
                r = m - 1
        return -1
            
        