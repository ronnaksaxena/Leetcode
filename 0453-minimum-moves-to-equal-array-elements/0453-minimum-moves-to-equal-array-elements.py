class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minVal = min(nums)
        return sum([x-minVal for x in nums])
    
    '''
    Since you have to increment n-1 elements you will need to increment the
    minimum element at least (maxE - minE) times and then all other elements will be incremented (x-minE) to catch to make them all equal
    
    '''
        