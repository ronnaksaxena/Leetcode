class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        '''
        [2,5,1,3,4,7]
         0,1,2,3,4,5
        [2,3,5,4,1,7]
         0,3,1,4,5,2
        [2,3,5,4,1,7]
             i
             x
                   y
        Time: O(n) where n is len(nums)
        Space: O(1) output array is returned at the end
        ''' 
        
        output = [0 for _ in range(2*n)]
        x, y = 0, n
        
        for i in range(0, 2 * n, 2):
            output[i] = nums[x]
            output[i+1] = nums[y]
            x += 1
            y += 1
            
        return output
        