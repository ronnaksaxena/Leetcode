class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        '''
        input: nums
        outpt: int

        is arr empty? -> No
        Does arr contain no 1/0s? => No
        Circular group ok

        Idea: keep track of zeros to replace between start and end 1

        Edge case: circular queue

        [0,1,0,0,1,0,0,0,0,1]

        '''

        def swap0():
            totalZeroes = sum(x == 0 for x in nums)
            if totalZeroes == 0 or totalZeroes == len(nums):
                return 0
            maxZeroWindow = 0

            for r in range(totalZeroes):
                if nums[r] == 0:
                    maxZeroWindow += 1
            
            l = 0
            windowZeroes = maxZeroWindow
            for r in range(totalZeroes-1, len(nums)):
                # Window is [l, ... r]
                maxZeroWindow = max(maxZeroWindow, windowZeroes)
                # update for next window
                if r < len(nums) - 1 and nums[r+1] == 0:
                    windowZeroes += 1
                if nums[l] == 0:
                    windowZeroes -= 1
                l += 1

            return totalZeroes - maxZeroWindow

        def swap1():
            totalOnes = sum(nums)
            if totalOnes == 0 or totalOnes == len(nums):
                return 0
            maxOneWindow = 0

            for r in range(totalOnes):
                if nums[r]:
                    maxOneWindow += 1
            
            l = 0
            windowOnes = maxOneWindow
            for r in range(totalOnes-1, len(nums)):
                # Window is [l, ... r]
                maxOneWindow = max(maxOneWindow, windowOnes)
                # update for next window
                if r < len(nums) - 1 and nums[r+1] == 1:
                    windowOnes += 1
                if nums[l]:
                    windowOnes -= 1
                l += 1

            return totalOnes - maxOneWindow

        return min(swap0(), swap1())
            
