class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        '''
        Notes:
        partition w pivot consists of sum[:pivot] == sum[pivot:]
        find # of pivots

        Clarificaitons:
        - input arr[int], int => output int
        - can have negatives
        - input array not empty
        - return 0 if no valid pivots

        nums = [2,-1,2], k = 3

        Brute Froce O(n^2)
        1. find max # of partitions from original array & from swapping k with each individual array
        2. find valid parition sum(leftSubArray) == sum(rightArray)
            - prefix Sum
        
        [2,-1,2]
    old [2, 1, 2]
        k
        [-1, -2, 0]

        the rest (- arr[i] + k) for i
        '''

        # init prefix sum array
        preSum = [nums[0]]
        for i in range(1, len(nums)):
            preSum.append(nums[i] + preSum[-1])


        def isValidPivot(pivot, swapIndex, swapValue):
            nonlocal preSum
            leftSub = preSum[pivot-1] if pivot > 0 else 0
            if swapIndex <= (pivot-1):
                leftSub = leftSub - swapValue + k
            rightSub = preSum[-1] - (preSum[pivot-1] if pivot > 0 else 0)
            if pivot <= swapIndex:
                rightSub = rightSub - swapValue + k
            return leftSub == rightSub

        def countValidPivots(arr, swapIndex, swapValue):
            return sum(isValidPivot(pivot, swapIndex, swapValue) for pivot in range(1, len(arr)))


        # see how many valid pivots in original array
        maxPivots = 0
        for pivot in range(1, len(nums)):
            leftSub = preSum[pivot-1] if pivot > 0 else 0
            rightSub = preSum[-1] - (preSum[pivot-1] if pivot > 0 else 0)
            maxPivots += (leftSub == rightSub)

        # try to swap each elem with k
        for i in range(len(nums)):
            old_val = nums[i]
            nums[i] = k
            maxPivots = max(maxPivots, countValidPivots(nums, i, old_val))
            nums[i] = old_val

        
        return maxPivots