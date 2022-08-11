class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # Helper fn to find angle between location and point
        def getAngle(p):
            angle = math.atan2(location[0]-p[0],location[1]-p[1]) / (2 * math.pi) * 360
            
            if angle < 0:
                angle += 360
            return angle
        
        
        angles = []
        res = 0
        # Account for edge case where point is same as location
        same = 0
        for p in points:
            if p == location:
                same += 1
            else:
                angles.append(getAngle(p))
        
        angles.sort()
        # Use sliding window to find all points visible from angle
        q = deque()
        for a in angles:
            
            q.append(a)
            # Pop all angles from queue outside window
            while a - q[0] > angle:
                q.popleft()
            res = max(res, len(q))
        
        for a in angles:
            a += 360
            
            q.append(a)
            # Pop all angles from queue outside window
            while a - q[0] > angle:
                q.popleft()
            res = max(res, len(q))
        
        return res + same
            
                
        
        
        
        
            
            
        
        
