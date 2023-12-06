class Solution:
    def totalMoney(self, n: int) -> int:
        startAmt = 0
        totalMoney = 0
        while n >= 1:
            startAmt += 1
            for i in range(7):
                if n == 0:
                    break
                totalMoney += startAmt + i
                n -= 1
        return totalMoney
                
        