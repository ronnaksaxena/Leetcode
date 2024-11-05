class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        '''
        [1,2,3,4], heaters = [1,4]
         0 1 1 1
        '''
        n = len(heaters)
        def bSearch(heaters, housePos):
            l, r = 0, len(heaters)
            while l < r:
                m = l + (r-l)//2
                if heaters[m] == housePos:
                    return m
                elif housePos > heaters[m]:
                    l = m + 1
                else:
                    r = m
            return l


        heaters.sort()

        minRadius = 0
        for house in houses:
            
            i = bSearch(heaters, house)
            if i < n and heaters[i] == house:
                continue
            # We know no heaters is at exact positons
            leftDistance = house - heaters[i-1] if i > 0 else float('inf')
            rightDistance = heaters[i] - house if i < n else float('inf')
            closestDistance = min(leftDistance, rightDistance)
            minRadius = max(minRadius, closestDistance)

        return minRadius



        