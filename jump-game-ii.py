class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0 #jumps and window starts at 0
        
        #BFS until window expands to end of nums
        while r < len(nums)-1:
            furthestJump = 0
            #find furthest index to jump to
            for i in range(l,r+1):
                furthestJump = max(furthestJump, nums[i]+i)
            
            #update window
            l,r = r+1, furthestJump
            jumps += 1
            
        return jumps
        
