class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
         
            l, r = 0, len(nums)
            
            while l < r:
                
                mid = l + (r-l)//2
                
                if nums[mid] < target:
                    l = mid + 1
                    
                else:
                    r = mid
                    
            return r
