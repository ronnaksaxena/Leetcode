class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        Q's
        - input: arr[int], k: int
        - output: int
        - valid input
        - nums only has 1 and 0

        nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

        Brute Force: - iterate through all subarrays and find longest array with <= k 0's

        [1,1,1,0,0,0,1,1,1,1,0]
                   l
                             r

        time: O(n)
        space: O(1)

        '''
        zeroCount = 0
        l = 0
        maxLength = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[l] == 0:
                    zeroCount -= 1
                l += 1
            maxLength = max(r-l+1, maxLength)
        return maxLength

        