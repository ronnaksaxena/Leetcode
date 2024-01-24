class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        x^n => x * x * x ... n times
        x^-n => 1/ x^n
        
        Brute force O(n):
            multiple x n times or 1 / x^n if n negative
        
        x^4 => x^2 * x^2
        if n is odd:
            x^5 => x^1 * x^2 * x^2
        
        Optimization: Binary search for pow
            BASE CASES:
            n < 0: divide answer by 1/ positive exp
            n == 0: return 1
            n == 1: return x
            if n odd:
                - x * rec(x, (n-1))
            if n even
                - rec(x, n // 2) * rec(x, n //2)
        '''
        
        if n < 0:
            return 1 / self.myPow(x,abs(n))
        elif n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n%2 == 1:
            return x * self.myPow(x,n-1)
        else:
            return self.myPow(x*x,n//2)
        