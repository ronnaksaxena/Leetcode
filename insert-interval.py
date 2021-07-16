class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
​
        output = []
        idx = 0
        newStart, newEnd = newInterval[0], newInterval[1]
        n = len(intervals)
        
        while idx < n and intervals[idx][0] < newStart:
            output.append(intervals[idx])
            idx += 1
            
        if not output or output[-1][1] < newStart:
            output.append(newInterval)
        else:
            output[-1][1] = max(newEnd, output[-1][1])
        
        while idx < n:
            curStart, curEnd = intervals[idx]
            idx += 1
            
            if curStart > output[-1][1]:
                output.append([curStart,curEnd])
            else:
                output[-1][1] = max(output[-1][1],curEnd)
        
        return output
                
