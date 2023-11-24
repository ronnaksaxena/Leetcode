class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxA = 0
        horizontalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts.sort()
        verticalCuts = [0] + verticalCuts + [w]
        
        maxH = 0
        for i in range(1, len(horizontalCuts)):
            maxH = max(maxH, horizontalCuts[i] - horizontalCuts[i-1])

        maxW = 0
        for j in range(1, len(verticalCuts)):
            maxW = max(maxW, verticalCuts[j] - verticalCuts[j-1])

        return (maxH * maxW) % (10**9 + 7)
                
                