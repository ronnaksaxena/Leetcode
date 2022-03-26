class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        l, r = 0, n-1
        
        while l <= r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
                
        return -1
            
            
        
