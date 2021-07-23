class Solution:
    def addBinary(self, a: str, b: str) -> str:
​
        output = []
        carry = 0
        a = list(reversed(a))
        b = list(reversed(b))
        i = 0
        while i < len(b) and i < len(a):
            sum = int(b[i]) + int(a[i])
            if carry == 1:
                sum += 1
            carry = 1 if sum>=2 else 0
            output.append(str(sum%2))
            i += 1
        
        longer = a if max(len(a),len(b))==len(a) else b
        
        for j in range(i,len(longer)):
            val = int(longer[j])
            if carry == 1:
                val += 1
            carry = 1 if val>=2 else 0
            output.append(str(val%2))
        
        if carry==1:
            output.append('1')
        return ''.join(output[::-1])
        
            
