class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        '''
        [2,2,1,2,1]
        
        [1, 1, 2, 2, 2, 2]
        
        Algo:
        1. push all elems into a min heap
        2. stor maxVal = 1 # min possible answer
        3. pop from heap to satisfy conditons
            - only decrease if needed
            - first elem must be decreased to 1 if not already 1
            
        Greedy:
            maxNum = min(nextVal+1, maxNum)
        '''
        
        arr.sort()
        maxNum = 1
        for n in arr[1:]:
            maxNum = min(maxNum+1, n)
        return maxNum
        