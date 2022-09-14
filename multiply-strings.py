class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        res = 0 # Will sum every layer calculated to find product
        
        
        '''
        Want to iterate in reverse order
        123
          i <-
        456
          j <-
        
        '''
        
        for i in range(len(num1)-1, -1, -1):
            # Since we're constructing left -> right
            curSum = collections.deque()
            level = len(num1)-1 - i
            curSum.append('0' * level)
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                product = int(num2[j]) * int(num1[i]) + carry
                digit = product % 10
                carry = product // 10
                # Building form left to right
                curSum.appendleft(str(digit))
                
            if carry:
                curSum.appendleft(str(carry))
            res += int(''.join(curSum))
            
        return str(res)
                
                
        
