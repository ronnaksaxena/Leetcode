class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = set(jewels)
        count = 0
        for c in stones:
            if c in jewelSet:
                count += 1
                
        return count
