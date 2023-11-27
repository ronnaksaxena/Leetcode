class Solution:
    def maxDiff(self, num: int) -> int:
        # Maximize a
        # Minimize b
        a = b = str(num)
        for d in a:
            if d != '9':
                a = a.replace(d, '9')
                break
        
        if b[0] != '1':
            b = b.replace(b[0], '1')
        else:
            for d in b[1:]:
                if d not in '10':
                    b = b.replace(d, '0')
                    break
        return int(a) - int(b)
        