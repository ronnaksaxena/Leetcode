class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        count = 0
        
        l, r = 0, len(nums)-1
        
        while l < r:
            #check if sum == k
            val = nums[l] + nums[r]
            if val < k:
                l += 1
            elif val > k: #TOO BIG
                r -= 1
            else:
                #found match
                count += 1
                l += 1
                r -= 1
                
        return count
        
