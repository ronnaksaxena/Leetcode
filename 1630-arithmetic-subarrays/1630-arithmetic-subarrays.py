class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArithmetic(l,r):
            sub = nums[l:r+1]
            sub.sort(reverse=True)
            return all(a-b == sub[1]-sub[0] for a,b in zip(sub[1:], sub))
        
        output = []
        for l,r in zip(l, r):
            output.append(isArithmetic(l,r))
        return output
        
        
        