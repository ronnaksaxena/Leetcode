class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        locX, locY = location[0], location[1]
        pAngles = []
        locCount = 0
        
        # find angle from location O(P)
        for point in points:
            xp, yp = point[0], point[1]
            if (yp - locY) == 0 and (xp - locX) == 0:
                locCount += 1
                continue
            else:
                pAngle = math.degrees(math.atan2((xp - locX), (yp - locY)))
            pAngles.append(pAngle)
        
        # Add same angles in quadrant but from 180 to 540
        # explain in the above graphics
        pAngles += [a + 360 for a in pAngles] # O(P)
        # sort so we can slide window # O(P log(P))
        pAngles.sort()
        
        # print(pAngles)
        
        # Sliding Window to find maximum subarray within the angle given # O(P)
        maxCount = 0
        l, r = 0, 0
        while r < len(pAngles):
            while r < len(pAngles) and pAngles[r] <= pAngles[l] + angle:
                r += 1
            maxCount = max(maxCount, r - l)
            l += 1
        
        return maxCount + locCount