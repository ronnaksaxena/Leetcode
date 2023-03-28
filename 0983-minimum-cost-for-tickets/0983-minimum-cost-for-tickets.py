class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        cost = 0
        # Front of queue will always be the least expensive ticket that is still valid that day
        dp7 = deque() # queue is of day, min_cost_so_far
        dp30 = deque()
        
        for d in days:
            # remove all values from the queue that expired before this day
            '''
            why <= ?
            ex. dp7 = [(1, 20)] and d == 8 then that ticket expired today and you have to buy another one
            but ticket for [(2, 40)] is still valid
            '''
            while dp7 and dp7[0][0] <= d-7:
                dp7.popleft()
            while dp30 and dp30[0][0] <= d-30:
                dp30.popleft()
                
            dp7.append((d, cost + costs[1]))
            dp30.append((d, cost + costs[2]))
            
            cost = min(cost+costs[0],dp7[0][1],dp30[0][1])
            
            
        return cost