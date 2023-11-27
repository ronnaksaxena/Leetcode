class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minStep = inf
        runningSum = 0
        for n in nums:
            runningSum += n
            minStep = min(minStep, runningSum)
        return 1 + (-1*minStep) if minStep < 1 else 1
        