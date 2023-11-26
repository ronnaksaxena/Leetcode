class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = list(range(1,n+1))
        i = 0
        while len(l) > 1:
            i = (i + k - 1)%len(l)
            l.pop(i)
        return l[0]
        