class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minVal = min(nums)
        return sum([x-minVal for x in nums])
        