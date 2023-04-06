class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''
        if n == 1 or n == 2:
            return n
        
        first, second = 1, 2
        # n + 1 becuase want to go to the nth fib number
        for _ in range(3, n+1):
            first, second = second, first + second
        # On last iteration second will store calculated nth fib number
        return second
        