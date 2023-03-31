class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Find pivot
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        if nums[pivot] <= target <= nums[-1]:
            l, r = pivot, len(nums) -1
        else:
            l, r = 0, pivot -1
            
        # Regular BSearch
        while l <= r:
            m = l + (r-l)// 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        # Target not in array
        return -1 
                
        
        