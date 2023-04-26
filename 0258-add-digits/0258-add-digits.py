class Solution:
    def addDigits(self, num: int) -> int:
        res = sum([int(d) for d in str(num)])
        while len(str(res)) > 1:
            res = sum([int(d) for d in str(res)])
        return res
        