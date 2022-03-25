class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        
        '''
        [10,20], [20, 0], [30, 50], [40, 40]
        
        
        
        '''
        
        costs.sort(key=lambda x: x[0]-x[1])
        
        total = 0
        n = len(costs) // 2
        
        for i in range(n):
            total += costs[i][0] + costs[i+n][1]
            
        return total
