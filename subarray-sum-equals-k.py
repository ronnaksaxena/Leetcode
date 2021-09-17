class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        curSum = 0
        res = 0
        prefix = collections.defaultdict(int)
        prefix[0] = 1
        
        for n in nums:
            curSum += n
            diff = curSum - k
            
            if diff in prefix:
                res += prefix[diff]
                
            prefix[curSum] += 1
            
        return res
        
