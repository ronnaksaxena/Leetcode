class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        output = set()
        
        def backtrack(start = 0):
            if start == len(nums):
                output.add(tuple(nums))
                return
            for i in range(start+1):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1)
                nums[start], nums[i] = nums[i], nums[start]
            
        
        backtrack()
        return [list(x) for x in list(output)]
        