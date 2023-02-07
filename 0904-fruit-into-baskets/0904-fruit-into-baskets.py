class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        [1,2,3,1,2]
           l
               r
        
        set = {2}
        maxFruit = 2
        Time: O(n) n == number of fruit
        Space: O(1) since length of set will never exceed constant 2
        '''
        maxFruit = 0
        # Need to keep track of last occurance of each fruit
        basket = collections.defaultdict(lambda: -1)
        l = 0
        for r in range(len(fruits)):
            if len(basket.keys()) < 2:
                basket[fruits[r]] = r
            elif fruits[r] not in basket:
                # Need to make space for this fruit in basket
                trashedFruit = min(basket, key=basket.get)
                l = basket[trashedFruit] + 1
                basket.pop(trashedFruit)
                basket[fruits[r]] = r
            basket[fruits[r]] = max(basket[fruits[r]], r)
            maxFruit = max(maxFruit, r - l + 1)
            
        return maxFruit
                
                
                
        