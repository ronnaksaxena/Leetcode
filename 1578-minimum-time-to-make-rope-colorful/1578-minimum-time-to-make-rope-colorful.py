class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        '''
        [a,a,b,a,a]
        [1,2,3,4,1]
                   i
    cost = 2
    maxRemoval = 4
    currentSum = 5
    
    Algo:
    loop thorugh baloons
    1. (if i >= 0 and colors[i] != colors[i-1]) or i == len(colors)
        compute cost
        reset vars
    2. curSum += neededTime[i]
        maxRemoval = max(maxRemoval, neededTime[i])
        
        '''
        
        cost = 0
        maxRemoval = 0
        currentSum = 0
        
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i-1]:
                cost += (currentSum-maxRemoval)
                currentSum = 0
                maxRemoval = 0
            maxRemoval = max(maxRemoval, neededTime[i])
            currentSum += neededTime[i]
        # Final group
        cost += currentSum - maxRemoval
        return cost
        