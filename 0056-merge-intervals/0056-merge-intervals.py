class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        input: list of interval lists
        output: list of interval lists
        
        - unsorted interval list
        - both start and end are inclusive
        
        Idea: Build non overlapping intervals list
        
        - sort the interval array by start time
        
        [[1,3],[2,6],[8,10],[15,18]]
           i
        output = [[1,6], [8,10], [15,18]]
           
        check if we should merge this interval with previous interval
        OR start new interval
        
        Algo:
        1. sort intervals by start
        2. init output list
        3. loop thorught intervals
            - if len(output) > 1 and output[-1][1] >= startTime
                - merge
            - else: add new interval to output
        4. return output
        
        Time: O(nlogn) to sort intervals
        Space: O(1)
        '''
        intervals.sort(key=lambda x: x[0])
        
        output = []
        
        for start, end in intervals:
            if output and output[-1][1] >= start:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start,end])
        
        return output
        