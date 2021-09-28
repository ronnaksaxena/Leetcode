class Solution:
    def isNumber(self, s: str) -> bool:
        
        digit, eeseen, dot = False, False, False
        sign = 0
        
        for i in range(len(s)):
            
            if s[i].isnumeric():
                digit = True
            elif s[i] == 'e' or s[i] == 'E':
                if not digit or eeseen:
                    return False
                if i == len(s) - 1:
                    return False
                eeseen = True
            elif s[i] == '.':
                if i == len(s) - 1 and not digit:
                    return False
                if dot:
                    return False
                if i > 0 and eeseen:
                    return False
                dot = True
            elif s[i] == '+' or s[i] == '-':
                if sign > 2:
                    return False
                if i>0 and ((s[i-1] != 'e' and s[i-1] != 'E')):
                    print('here')
                    return False
                if i == len(s) - 1:
                    return False
                sign += 1
                
            else:
                return False
            
        return True
        
