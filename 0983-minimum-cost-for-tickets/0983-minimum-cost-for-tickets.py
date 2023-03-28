class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost = 0
        dp7 = collections.deque() # day, minCost
        dp30 = collections.deque()
        
        for d in days:
            # remove all expired tickets
            while dp7 and dp7[0][0] <= d-7:
                dp7.popleft()
            while dp30 and dp30[0][0] <= d-30:
                dp30.popleft()
            
            dp7.append((d, cost + costs[1]))
            dp30.append((d, cost + costs[2]))
            
            cost = min(cost + costs[0], dp7[0][1], dp30[0][1])
            
        return cost
        