class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        [-2,1,-3,4,-1,2,1,-5,4]
        
        if elem + localMaxSum > elem:
            localMaxSum += elem
        else:
            localMaxSum = elem
        globalMaxSum = max(globalMaxSum, localMaxSum)
        
        globalMaxSum = -inf
        localMaxSum = -inf
        
        '''
        
        globalMaxSum = float('-inf')
        localMaxSum = float('-inf')
        
        for n in nums:
            if n + localMaxSum > n:
                localMaxSum += n
            else:
                localMaxSum = n
            globalMaxSum = max(globalMaxSum, localMaxSum)
            
        return globalMaxSum
        