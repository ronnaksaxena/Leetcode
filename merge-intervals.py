class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for start,end in intervals[1:]:
            if start <= res[-1][1]:
                newStart = min(res[-1][0], start)
                newEnd = max(res[-1][1], end)
                res.pop()
                res.append([newStart, newEnd])
            else:
                res.append([start,end])
        
        return res
        
               
               
        
