class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # If you XOR every elem the final result will be single num
        res = 0
        for n in nums:
            res ^= n
            
        return res
