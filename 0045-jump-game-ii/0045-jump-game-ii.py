class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        [2,3,1,1,4]
               s
                 e
        
        jumps = 2
        '''
        
        start, end = 0, 0
        jumps = 0
        
        while end < len(nums) - 1:
            furthestJump = end
            for i in range(start, end+1):
                furthestJump = max(furthestJump, nums[i] + i)
            start = end + 1
            end = furthestJump
            jumps += 1
            
        return jumps
        