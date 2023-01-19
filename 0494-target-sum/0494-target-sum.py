class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        p1 + p2 = sum
        p1  - p2 = target
        p1 - (sum-p1) = target
        2p1 - sum = target
        val = (target+sum) // 2

        Edge cases:
        if abs(target) > sum(num) can't sum to it
        if target is odd than not 2 partitions can equal it
        '''

        numSum = sum(nums)
        n = len(nums)
        if abs(target) > numSum:
            return 0
        if (target+numSum) % 2 == 1:
            return 0
        val = (target + numSum) // 2
        DP = [[0 for _ in range(val+1)] for _ in range(n+1)]
        DP[0][0] = 1

        for i in range(1, len(DP)):
            for j in range(len(DP[0])):
                if nums[i-1] <= j:
                    DP[i][j] = DP[i-1][j] + DP[i-1][j-nums[i-1]]
                else:
                    DP[i][j] = DP[i-1][j]

        return DP[-1][-1]




