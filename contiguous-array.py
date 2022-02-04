class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        map = collections.defaultdict(int)
        preSum = 0
        maxLen = 0
        map[0] = -1
        
        for i in range(len(nums)):
            preSum += nums[i] if nums[i] == 1 else -1
            if (preSum) in map:
                maxLen = max(maxLen, i-map[preSum])
            else:
                map[preSum] = i
                
        return maxLen
        
        
'''
0   1   0   0   1   1   0
        i   
​
maxLen = 2
sum = -1
map:
0: -1
-1: 0
​
​
