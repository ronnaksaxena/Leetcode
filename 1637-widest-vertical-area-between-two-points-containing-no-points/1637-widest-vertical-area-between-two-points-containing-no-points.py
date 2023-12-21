class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maxWidth = 0
        points.sort(key = lambda x: x[0])
        for i in range(1, len(points)):
            x1, _ = points[i]
            x2, _ = points[i-1]
            maxWidth = max(maxWidth, x1-x2)
        return maxWidth
        