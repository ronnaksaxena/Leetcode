class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        max_end = float('-inf')
        
        for start,end in intervals:
            if start >= max_end:
                max_end = end
            else:
                count += 1
                
        return count
