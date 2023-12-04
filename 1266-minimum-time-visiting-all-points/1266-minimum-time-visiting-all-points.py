class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def findDistance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return max(abs(x2-x1), abs(y2-y1))
        
        ans = 0
        for i in range(1, len(points)):
            ans += findDistance(points[i-1], points[i])
        return ans