from typing import List
import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        def getAngle(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            deltaX = x2 - x1
            deltaY = y2 - y1

            radAngle = math.atan2(deltaY, deltaX)
            degrees = math.degrees(radAngle)
            if degrees < 0:
                degrees += 360
            return degrees

        def pointInWindow(startAngle, compareAngle, windowLength):
            endAngle = startAngle + windowLength
            if endAngle >= 360:
                return startAngle <= compareAngle < 360 or 0 <= compareAngle <= endAngle % 360
            else:
                return startAngle <= compareAngle <= endAngle

        # Filter points at the location itself
        filteredPoints = [p for p in points if p != location]
        samePoints = len(points) - len(filteredPoints)  # Number of points at the exact location
        if not filteredPoints:
            return len(points)

        # Calculate the angle of each point relative to the location
        angles = [getAngle(location, p) for p in filteredPoints]
        angles.sort()

        # Duplicate the angles array with +360 to handle circular wrap-around
        angles += [a + 360 for a in angles]

        # Sliding window over the sorted angle list
        maxCount = 0
        l = 0
        for r in range(len(angles)):
            while angles[r] - angles[l] > angle:
                l += 1
            maxCount = max(maxCount, r - l + 1)

        return maxCount + samePoints
