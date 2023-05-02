class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []
        i = 0
        
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1
        if output and output[-1][-1] >= newInterval[0]:
            output[-1] = [min(output[-1][0], newInterval[0]), max(output[-1][-1], newInterval[1])]
        else:
            output.append(newInterval)

        while i < len(intervals):
            start, end = intervals[i]
            if start <= output[-1][-1]:
                output[-1] = [min(output[-1][0], start), max(output[-1][-1], end)]
            else:
                output.append(intervals[i])
            i += 1
                
        return output
                          