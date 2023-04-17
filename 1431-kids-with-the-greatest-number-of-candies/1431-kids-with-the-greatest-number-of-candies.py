class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highestCandies = max(candies)
        n = len(candies)
        output = [False for _ in range(n)]
        
        for i, c in enumerate(candies):
            if extraCandies + c >= highestCandies:
                output[i] = True
        return output
        