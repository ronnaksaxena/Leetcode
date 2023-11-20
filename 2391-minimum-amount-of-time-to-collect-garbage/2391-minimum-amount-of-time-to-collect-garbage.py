class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        '''
        each truck takes count of trash in grabage[i] + travel time to pickup
        
        1. find furthest distance each truck should travel
        2. iterate to that distance for each truck and calculate time needed
        3. times needed for all trucks
        
        
        '''
        n = len(garbage)
        gStop, pStop, mStop = -1, -1, -1
        # Find ending value for all trucks
        for i in range(len(garbage)-1, -1, -1):
            g = garbage[i]
            if 'G' in g:
                gStop = max(gStop, i)
            if 'P' in g:
                pStop = max(pStop, i)
            if 'M' in g:
                mStop = max(mStop, i)
            
            if gStop >= 0 and mStop >= 0 and pStop >= 0:
                break
        minutes = len(garbage[0])
        # Find minutes for all trucks
        for i, g in enumerate(garbage[1:], 1):
            count = len(g)
            # How many trucks need to travel here
            mult = sum([i <= gStop, i <= pStop, i <= mStop])
            minutes += (count + travel[i-1] * mult)
        return minutes
            
        