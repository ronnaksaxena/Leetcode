class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        pointsSet = set()
        for x, y in points:
            pointsSet.add((x,y))

        minRectangle = float('inf')

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # Skip if points are in same vertical or horizontal line
                # as they can't form a rectangle
                if x1 == x2 or y1 == y2:
                    continue
                
                # Check if other two corners exist
                # (x1,y2) and (x2,y1) must exist to form rectangle
                if (x1, y2) in pointsSet and (x2, y1) in pointsSet:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    minRectangle = min(minRectangle, area)

        return minRectangle if minRectangle != float('inf') else 0
        