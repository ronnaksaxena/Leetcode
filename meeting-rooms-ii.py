class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(rooms, intervals[0][1])
        
        for i in range(1, len(intervals)):
            #check if room is empty or end time of top of heap <= start time of cur interval
            if rooms[0] <= intervals[i][0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, intervals[i][1])
        
        return len(rooms)
