class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        input: List[int], int
        output: int -> no of subarrays
        
        - [-1000,  1000]
        - Nums not null
        - empty array with k == 0: return 1
        
        [1,-1,1,-1,1], k = 1
                   i
         rs = 1
        
        How many subarrays from 0->i == k
        subArrSum = {sum: number of subarrays with sum}
        {
        0: 2,
        1: 2,
        }
        totalArrs = 5
        if runningSum - k in subArrSum:
            totalArr += subArrSum[runningSum-k]
        subArrSum[runningSum] += 1

        Brute force O(n^3)
        
        Prefix Sum A[i:j (inclisvie)] Sum(A[i]) - Sum(A[j-1] if j > 0 else 0)
        O(n^2)
        
        Cache Subarray sums
        Time O(n)
        Space: O(n)
        '''
        subArrSum = collections.defaultdict(int) # {sum: number of subarrays with sum}
        runningSum = 0
        totalArrs = 0
        subArrSum[0] = 1
        
        for n in nums:
            runningSum += n
            if (runningSum - k) in subArrSum:
                totalArrs += subArrSum[(runningSum - k)]
            subArrSum[runningSum] += 1
        
        return totalArrs
                
        
        
        
        
        
        
        