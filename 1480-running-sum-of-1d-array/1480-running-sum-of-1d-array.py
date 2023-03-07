class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [0 for _ in range(len(nums))]
        agSum = 0
        
        for i, n in enumerate(nums):
            agSum += n
            output[i] = agSum
            
        return output
            