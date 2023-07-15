'''
Algo:
1. Sort all events by start day
2. At each current day bSearch to find next potential choices of events
3. Return max pts

'''
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[0])
        lastStartDay = events[-1][0] # Used to check if we ran out of choices
        print(events)
        @cache
        def dp(day, kLeft):
            # Base Cases, out of choices or used up all events
            if day > lastStartDay or kLeft == 0:
                return 0
            # BSearch to find remaining possible choices
            l, r = 0, len(events)
            while l < r:
                m = l + (r-l)//2
                if day > events[m][0]:
                    l = m + 1
                else:
                    r = m
            maxPts = float('-inf')
            for start, end, pt in events[l:]:
                maxPts = max(maxPts, pt + dp(end + 1, kLeft-1))
            return maxPts
        
        return dp(1, k)
        