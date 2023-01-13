class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        nums = 2,
              / \
             3   1
             /\
            1  4
        Time: O(n)
        Space: O(1)
        PSUEDOCODE
        jumps = 0
        start, end = 0, 0
        furthestJump = 0
        while end < len(nums)-1:
            for i in range(start, end+1):
                furthestJump = max(furthestJump, i + nums[i])
            jumps += 1
            start = end + 1
            end = furthestJump
        return jumps
        
        [2,3,1,1,4]
               s
                  e
                  f
         
         j = 1
        
        '''
        
        jumps = 0
        furthestJump = 0
        start, end = 0, 0
        # Want to stop when window includes last element
        while end < len(nums)-1:
            for i in range(start, end+1):
                furthestJump = max(furthestJump, i + nums[i])
            jumps += 1
            start = end + 1
            end = furthestJump
        return jumps
        
        
        
        
        