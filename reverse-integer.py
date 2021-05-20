class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        sign = -1 if x<0 else 1
        digits = []
        if sign == 1:
            digits = [str(d) for d in str(x)]
        else:
            digits = [str(d) for d in str(x)[1:]]
        
        digits = digits[::-1]
        revNum = int(''.join(digits))
        return sign*revNum if -(2**31) < revNum < (2**31) else 0
