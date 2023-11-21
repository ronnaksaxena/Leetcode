class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        DP[i] = (min(leftHighest[i], rightHighest[i]) - heigh[i])
        '''
        n = len(height)
        leftHighest = [0] * n
        leftHighest[0] = height[0]
        rightHighest = [0] * n
        rightHighest[-1] = height[-1]
        for i in range(1, n):
            leftHighest[i] = max(leftHighest[i-1], height[i])
        for i in range(n-2, -1, -1):
            rightHighest[i] = max(rightHighest[i+1], height[i])
        water = 0
        for i in range(n):
            water += (min(leftHighest[i],rightHighest[i]) - height[i])
        return water