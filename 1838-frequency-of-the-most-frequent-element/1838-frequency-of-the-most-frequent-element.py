class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        '''
        n = [1,4,8.13]
             l
             r
        cur = 0
        
        while len of window * target - curr > k:
            curr -= n[l]
            l += 1
        maxFreq = max(maxFreq, r-l+1)
        r += 1
        
        '''
        nums.sort()
        curr = 0
        l = 0
        maxFreq = 1
        for r in range(len(nums)):
            curr += nums[r]
            while (r-l+1) * nums[r] - curr > k:
                curr -= nums[l]
                l += 1
            maxFreq = max(maxFreq, r-l+1)
        return maxFreq
        
        
        
        
        
        