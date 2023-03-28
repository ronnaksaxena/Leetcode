class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        '''
        days = [1,4,6,7,8,20]
        costs = [2,7,15]
        q = [(0,0)] -> (day, cost)
        minCost = float('inf')
        while q[0] <= curDay: -> all expired tickets
            day, cost = q.popleft()
            if cost < minCost: -> obtain lowest cost to make it to this day
                minCost = cost
            q.append((curDay + 1, minCost+costs[0])) -> 1 day pass
            q.append((curDay + 7, minCost+costs[1])) -> 7 day pass
            q.append((curDay + 30, minCost+costs[2])) -> 30 day pass
        # return the min money spent
        return min(q, key= lambda x: x[1])
        
        '''
        @cache
        def search(day_index, current_day):
            if day_index >= len(days):
                # vacation is over
                return 0
            if current_day > days[day_index]:
                # we're covered, keep searching
                return search(day_index+1, current_day)
            
            return min(
                costs[0] + search(day_index+1, days[day_index]+1),
                costs[1] + search(day_index+1, days[day_index]+7),
                costs[2] + search(day_index+1, days[day_index]+30)
            )
        
        return search(0, 0)
            
            
        