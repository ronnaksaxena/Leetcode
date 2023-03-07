class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # B search to find minimum number of time needed for all trips
        left, right = 1, max(time) * totalTrips
        
        def isEnoughTime(curTime):
            tripsDone = 0
            for t in time:
                tripsDone += curTime // t
                
            return tripsDone >= totalTrips
        
        while left < right:
            mid = left + (right-left) // 2
            if isEnoughTime(mid):
                right = mid
            else:
                left = mid + 1
                
        return left