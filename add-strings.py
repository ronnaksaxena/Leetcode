class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        output = deque()
        p1, p2 = len(num1) - 1, len(num2)-1
        carry = 0
        
        while p1 >= 0 or p2 >= 0:
            
            x1 = int(num1[p1]) if p1 >= 0 else 0
            x2 = int(num2[p2]) if p2 >= 0 else 0
            
            val = carry + x1 + x2
            digit = val % 10
            carry = val // 10
            output.appendleft(str(digit))
            p1 -= 1
            p2 -= 1
            
            
            
        if carry:
            output.appendleft(str(carry))
            
        return ''.join(output)
            
