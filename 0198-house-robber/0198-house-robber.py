class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        DP = [0 for _ in range(n+1)]
        # Base case if not houses max profit is 0
        # Base case: if 1 house that value is max profit
        DP[0], DP[1] = 0, nums[0]
        # Iterate from 2
        for i in range(2, len(DP)):
            # DP[i] = max(not robbing this house DP[i-1], or robbing this house DP[i-2] + nums[i])
            DP[i] = max(DP[i-2] + nums[i-1], DP[i-1])
        
        return DP[-1]
    '''
    Time: O(n)
    Space: O(n)
    '''
        