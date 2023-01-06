class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs.sort()
        for bar in costs:
            if bar <= coins:
                count += 1
                coins -= bar
            else:
                return count
        
        return len(costs)