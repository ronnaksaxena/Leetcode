class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        if len(uniqueNums) < 3:
            return max(uniqueNums)
        
        return heapq.nlargest(3, list(uniqueNums))[-1]
        