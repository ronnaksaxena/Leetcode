class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        '''
        costs = [3,2,7,7,1,2], k = 2, candidates = 2
                   l    r
                    
        pq = (cost, index)
        heap = [(1,4), (2, 1), (2, 5), (3, 0)]
        
        PSEUDOCODE
        loop k times:
            currentCost, _ = heap pop
            totalCost += currentCost
            if l > r:
        
        
        '''
        
        pq = []
        l, r = candidates - 1, len(costs) - candidates
        # Edge case if all candidates can be selected
        if candidates > len(costs) // 2:
            for i, c in enumerate(costs):
                heapq.heappush(pq, (c, i))
                l, r = len(costs), -1
        else:
            for i in range(candidates):
                # add left side
                heapq.heappush(pq, (costs[i], i))
                # add right side
                heapq.heappush(pq, (costs[len(costs)-1-i], len(costs)-1-i))
        
        totalCost = 0
        # pick k cheapest candidates
        for _ in range(k):
            curCost, i = heapq.heappop(pq)
            # print(curCost, i)
            # print(l, r)
            # print('\n')
            totalCost += curCost
            if i <= l:
                l += 1
                if l < r:
                    heapq.heappush(pq, (costs[l], l))
            else:
                r -= 1
                if r > l:
                    heapq.heappush(pq, (costs[r], r))
        return totalCost
            
                