class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        # one hour angle 30
        # one min angle 6
        
        minute_angle = minutes * 6
        hour_angle = (hour%12 + minutes / 60) * 30
        
        diff = abs(hour_angle-minute_angle)
        
        return min(diff, 360-diff)
        
