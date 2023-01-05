class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        [[10,16],[2,8],[1,6],[7,12]]
        sort by start time
        [[1,6], [2, 8], [7, 12], [10, 16]]
                ^
                |
        if curStart <= groupEnd:
            # Can add to group
            groupStart = max(groupStart, curStart)
            groupEnd = min(groupEnd, curEnd)
        else:
            # Have to create new group for arrow
            arrows += 1
            groupStart, groupEnd = curStart, curEnd
        
        
        groupStart = 1
        grouptEnd = 6
        arrows = 1
        '''
        points.sort(key=lambda x: x[0])
        arrows = 1
        groupStart, groupEnd = points[0][0], points[0][1]
        
        for curStart, curEnd in points[1:]:
            if curStart <= groupEnd:
                groupStart = max(groupStart, curStart)
                groupEnd = min(groupEnd, curEnd)
            else:
                arrows += 1
                groupStart, groupEnd = curStart, curEnd
        return arrows
        
        