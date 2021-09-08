class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if len(nums)==1:
            return nums[0]
        
        maxElem = nums[0]
        maxSum = 0
        
        for num in nums:
            maxElem = max(maxElem, num)
            maxSum += num
            
        lo, hi = maxElem, maxSum
        
        while lo < hi:
            mid = lo + (hi-lo)//2
            pieces = self.split(nums,mid)
            if pieces > m: #sum needs to be bigger for less groups
                lo = mid+1
            else:
                hi = mid #sum needs to be smaller for more groups
        return lo
    
    def split(self, nums, largestSum):
        pieces = 1
        tempSum = 0
        for num in nums:
            if num+tempSum > largestSum:
                pieces += 1
                tempSum = num
            else:
                tempSum += num
        return pieces
        
        
        
        
