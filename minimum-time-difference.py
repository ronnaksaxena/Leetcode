class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minDif = float('inf')
        for i in range(len(timePoints)):
            for j in range(i+1, len(timePoints)):
                # Extract minutes
                # 00:00
                minutesI = int(timePoints[i][:2]) * 60 + int(timePoints[i][3:])
                minutesJ = int(timePoints[j][:2]) * 60 + int(timePoints[j][3:])
                dif = abs(minutesI-minutesJ)
                minDif = min(dif, (60 * 24) - dif, minDif)
                if minDif == 0:
                    return 0
        return minDif
            
        
        
        
'''
60 * 24 = minutes in a day
1. find minutes at timePoint i and timePoint j
2. find difference : update min difference
minDif = min (abs(minI-minJ), (60 * 24) - abs(minI-minJ))
​
00:00 23:59
​
​
'''
