class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        maxW = float('-inf')
        for j in range(m):
            maxW = max(maxW, sum(accounts[j]))
                       
                       
        return maxW
        
