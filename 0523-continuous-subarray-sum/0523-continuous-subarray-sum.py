class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        - no negative numbers, can be 0s
        - k is positive
        - nums not null
        - no integer overflow
        
        Brute Force: Check all subarrays and sum elements O(N^3)
        Brute force w prefix sums: Check all subarrays and see if prefix sum mult of k O(N^2)
        Optimal: Storing runningSum O(n)
        
        prefixSum = {remainder of prefixSum: index} => O(k)
        
        
        nums = [23,2,4,6,7], k = 6
        remain [5, 1, 5]
                  [ k  ]
                  4 could be 10, 16, 22, etc
        If duplicate remainders, we have a subarray that is divisible by k
        
        Need to handle edge case of 00s
        
        '''
        if len(nums) <= 1:
            return False
        runningSum = 0
        prefixSums = {0: -1}
        
        for i in range(len(nums)):
            
            runningSum += nums[i] 
            runningSum %= k # Find remainder
            # There is a subarray with a multiple of k
            if runningSum in prefixSums:
                if (i - prefixSums[runningSum]) >= 2:
                    return True
            else:
                prefixSums[runningSum] = i # Only map if it is not 0
            
        return False
        