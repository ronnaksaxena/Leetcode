class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        first, second, third = 0, 1, 1
        for _ in range(3, n+1):
            first, second, third = second, third, first + second + third
            
        return third
            
        