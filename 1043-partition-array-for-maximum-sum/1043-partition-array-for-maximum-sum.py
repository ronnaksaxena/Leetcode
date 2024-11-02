class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def dp(i):
            if i == -1:
                return 0
            if i == 0:
                return arr[0]
            
            ans = 0
            largestElem = float('-inf')
            for j in range(i, max(-1, i - k), -1):
                largestElem = max(largestElem, arr[j])
                countOfElem = i-j+1
                ans = max(ans, (countOfElem * largestElem) + dp(j-1))
            return ans


        return dp(len(arr)-1)
        