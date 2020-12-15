class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        leftMax = [0] * len(seats)
        rightMax = [0] * len(seats)
        maxDist = 0
        
        leftMax[0] = 0 if seats[0]==1 else 1
        for i in range(1,len(seats)):
            if seats[i]==0:
                leftMax[i] = leftMax[i-1]+1
            else:
                leftMax[i] = 0
        
        rightMax[-1] = 0 if seats[-1]==1 else 1
        for i in range(len(seats)-2,-1,-1):
            if seats[i]==0:
                rightMax[i] = rightMax[i+1]+1
            else:
                rightMax[i] = 0
        for i in range(len(seats)):
            dist = min(leftMax[i],rightMax[i])
            if i==0:
                dist = rightMax[i]
            if i==len(seats)-1:
                dist = leftMax[i]
            maxDist = max(maxDist,dist)
