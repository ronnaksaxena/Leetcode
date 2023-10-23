class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        x = 4
        while x < n:
            x *= 4
        return x == n
        