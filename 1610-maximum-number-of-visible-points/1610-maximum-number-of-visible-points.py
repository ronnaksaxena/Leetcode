class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        '''
        Need helper fn to find angle
                     p2
                  / |
                /   |
              /     | O
           /        |
         / X        |
        p1----------
             A

        tan(x) = O/A
        x = atan(o/a) => atan((y2-y1) / (x2-x1))

        Steps:
        1. Count how many pts == starting location and remove them
        2. Sort remainig pts by angle relative to x axis and + 360 to avoid loop
        3. Sliding window to find max pts that fit in angle

        Time: O(NlogN) to sort + O(N) to slide through window
        Space: O(n) to store other angles // can omit

        '''

        def getAngle(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            deltaX = x2-x1
            deltaY = y2-y1

            radAngle = math.atan2(deltaY, deltaX)
            degAngle = math.degrees(radAngle)
            if degAngle < 0:
                degAngle += 360
            return degAngle

        filteredPoints = [p for p in points if p != location]
        if not filteredPoints:
            return len(points)
        samePoints = len(points) - len(filteredPoints)
        angles = [getAngle(location, p)for p in filteredPoints]
        angles.sort()


        angles += [a + 360 for a in angles]
        '''
        ex:
        angle is 40
        angles = [10, 20, 30, 340, 350]
        angles = [10, 20, 30, 340, 350, 370, 380, 390, 700, 710]
                               l                    r
                                                    30

        '''
        maxWindow = 0
        l = 0
        # print(angles)
        for r in range(len(angles)):
            # 10 20 50
            #       r
            #       l
            while angles[r] - angles[l] > angle:
                l += 1
            # print(f'l {l} r {r}')
            maxWindow = max(maxWindow, r-l+1)

        return maxWindow + samePoints

        