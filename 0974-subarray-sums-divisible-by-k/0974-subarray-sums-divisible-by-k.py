class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''
        [4,5,0,-2,-3,1]
        
        k = 5
        
        count = [1, 0, 0, 0, 3, 0, 0]
        pre = 4
        res = 3
        '''
        A = nums
        res = 0
        prefix = 0
        count = [1] + [0] * k
        for a in A:
            prefix = (prefix + a) % k
            res += count[prefix]
            count[prefix] += 1
        return res
        