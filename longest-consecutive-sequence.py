class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set(nums)
        maxLen = 0
        
        for n in numSet:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                    
                maxLen = max(maxLen, length)
                
        return maxLen
