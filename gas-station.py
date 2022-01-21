class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        totalTank, curTank = 0, 0
        starting = 0
        
        for i in range(n):
            
            curTank += gas[i] - cost[i]
            totalTank += gas[i] - cost[i]
            
            if curTank < 0:
                starting = i + 1
                curTank = 0
                
        return starting if totalTank >= 0 else -1
                
                
                
