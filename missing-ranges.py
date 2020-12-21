class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        prev = lower-1
        for i in range(0,len(nums)+1):
            cur = nums[i] if i<len(nums) else upper+1
            if prev+1 <= cur-1:
                res.append(self.formatRange(prev+1,cur-1))
            prev = cur
        return res
    
    def formatRange(self,lower,upper):
        if lower==upper:
            return str(lower)
        else:
            return str(lower)+'->'+str(upper)
