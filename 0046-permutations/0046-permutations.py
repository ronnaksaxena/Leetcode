class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        [1,2,3]
        
        /     |     \
    [2,1,3]  [1, 2, 3]
    / \
[2, 3, 1] [2, 1, 3]
        
        '''
        
        output = []
        
        def backtrack(cur, i):
            nonlocal output
            if i == len(nums):
                output.append(cur[::])
                return

            for j in range(i, len(nums)):
                cur[i], cur[j] = cur[j], cur[i]
                backtrack(cur, i+1)
                cur[i], cur[j] = cur[j], cur[i]
                
        backtrack(nums, 0)
        return output
                    
                
                
        