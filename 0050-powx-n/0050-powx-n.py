class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        key idea: x^n == (x*x)^(n//2) if n is even
        Time: LogN
        Space: LogN
        '''
        
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n < 0:
            return 1.0 / self.myPow(x, n * -1)
        
        elif n%2 == 1:
            return x * self.myPow(x*x, (n-1)//2)
        
        else:
            return self.myPow(x*x, n // 2)
        
        