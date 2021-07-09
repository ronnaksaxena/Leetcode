class Solution:
    def reverse(self,nums,L,R):
        while L<R:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1
            
            
            
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        plantIdx = -1
        for i in range(len(nums)-1, 0,-1):
            if nums[i] > nums[i-1]: #finds plant
                plantIdx = i-1
                break
        if plantIdx == -1: #no nextPerm
            self.reverse(nums,0,len(nums)-1)
            return
        
        nextGreatest = float('inf')
        NGI = -1
        for i in range(len(nums)-1, plantIdx, -1):
            if nums[i] > nums[plantIdx] and nums[i] < nextGreatest:
                nextGreatest = nums[i]
                NGI = i
                
        if NGI == -1: #no elem greater to the right
            return
        
        #swap plant with next perm
        nums[plantIdx], nums[NGI] = nums[NGI], nums[plantIdx]
        #reverse rest
        self.reverse(nums,plantIdx+1, len(nums)-1)
        
        return
        
        
        
        
        
        
        
