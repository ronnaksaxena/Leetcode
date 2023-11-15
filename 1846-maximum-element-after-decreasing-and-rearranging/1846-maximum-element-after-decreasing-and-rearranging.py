class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        ''' 
        Greedy:
            maxNum = min(nextVal+1, maxNum)
        '''
        arr.sort()
        maxNum = 1
        for n in arr[1:]:
            maxNum = min(maxNum+1, n)
        return maxNum
        