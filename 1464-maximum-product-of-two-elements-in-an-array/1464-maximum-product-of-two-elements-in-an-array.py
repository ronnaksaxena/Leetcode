class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest = 0
        secondBiggest = 0
        for n in nums:
            if n >= biggest:
                second = biggest
                biggest = n
            else:
                second = max(second, n)
        return (biggest-1) * (second-1)
                
        