class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        '''
        [2,3,1,1,4]
                 c
                 j
                 
        if nums[c] >= furthestJump:
            furthestJump = c
            
        return c == 0
        time: O(n)
        Space: O(1)
        
        '''
        
        
        furthestJump = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= furthestJump:
                furthestJump = i
        
        return furthestJump == 0
        
        