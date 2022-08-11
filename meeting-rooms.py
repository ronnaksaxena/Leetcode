class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        
        intervals.sort(key=lambda x: x[0])
        prev_end = intervals[0][1]
        
        for start,end in intervals[1:]:
            # Conflicting meeting time
            if start < prev_end:
                return False
            else:
                prev_end = end
        return True
        
