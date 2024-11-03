class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        '''
        [1,2,3,4], heaters = [1,4]
                             l   r
                                m
         0 1 1 1

        Case 1: heater is at house pos: radius needed is 0
         We know ther is no heater at house position
        Case 2: closest heater is left of house pos
            if i != 0: radius needed is h - heaters[i-1]
        Case 3: closest heater is right of house pos
            if i != n: radius needed is heaters[i] - h

        Find min(case2, case3)
        Whatever max readius needed for all houses is min global radius

        EDGE CASES:
            no houses no heaters
            all heaters earlier than house pos
            all heaters after house pos
            LOT of heaters
        '''
        def bSearch_left(housePos):
            l, r = 0, len(heaters)
            while l < r:
                m = l + (r-l)//2
                if heaters[m] == housePos:
                    return m
                    # WHY? Since current heater pos < housePos: we must insert to left half
                elif heaters[m] < housePos:
                    l = m + 1
                else:
                    r = m
            return l

        heaters.sort()
        minRadius = 0

        for housePos in houses:

            houseIndex = bSearch_left(housePos)
            # print(f'housePos {housePos} i {houseIndex}')
            if houseIndex != len(heaters) and heaters[houseIndex] == housePos:
                continue
            
            closestLeft = housePos - heaters[houseIndex-1] if houseIndex != 0 else float('inf')
            closestRight = heaters[houseIndex] - housePos if houseIndex != len(heaters) else float('inf')

            minRadius = max(min(closestLeft, closestRight), minRadius)

        return minRadius

        