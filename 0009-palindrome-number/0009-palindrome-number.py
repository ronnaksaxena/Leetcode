class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if neg not palnedrome
        if x < 0:
            return False
        # Returns the power of the 10 that a number is
        def getDigitPow(num):
            res = 1
            while num:
                num = num // 10
                res *= 10
            return res // 10 #off by one
        
        left, right = getDigitPow(x), 10
        # 2 pointer
        while left >= right:
            # Get left and right digits
            lDigit, rDigit = (x // left)%10, (x % right) // (right // 10)
            if lDigit != rDigit:
                return False
            
            left = left//10
            right *= 10
            
        return True
            
            
        