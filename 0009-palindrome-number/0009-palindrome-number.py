class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if neg not palnedrome
        if x < 0:
            return False
        def getDigitPow(num):
            res = 1
            while num:
                num = num // 10
                res *= 10
            return res // 10 #off by one
        
        left, right = getDigitPow(x), 10
        while left >= right:
            lDigit, rDigit = (x // left)%10, (x % right) // (right // 10)
            # print(left, right, lDigit, rDigit)
            if lDigit != rDigit:
                return False
            
            left = left//10
            right *= 10
            
        return True
            
            
        