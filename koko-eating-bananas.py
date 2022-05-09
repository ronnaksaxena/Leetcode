class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        binary searching between 0 and max(piles)
        min value of k bananas eaten per hour will not exceed val to eat all bananas in pile every hour
        
        '''
        
        l, r = 1, max(piles)
        
        while l < r:
            
            m = l + (r-l)//2
            #number of hours taken to eat m bananas per hour
            speed = 0
            
            for p in piles:
                
                #how many hours to eat all bananas in pile
                #ceil becuase it takes an entire hour if there are < m bananas in pile
                speed += math.ceil(p/m)
                
            if speed <= h:
                #can eat all bananas at rate of m per hour
                r = m
            else:
                #need to eat more bananas per hour
                l = m + 1
        return r
                
        
