class Solution:
    def calculate(self, s: str) -> int:
        curNum, prevSign = 0, '+'
        stack = []
        s = s.replace(' ', '')
        
        for i in range(len(s)):
            
            if s[i].isnumeric():
                curNum = curNum*10 + int(s[i])
                
            if s[i] in '+-/*' or i == len(s)-1:
                if prevSign == '+':
                    stack.append(curNum)
                elif prevSign == '-':
                    stack.append(curNum * -1)
                elif prevSign == '*':
                    mrc = stack.pop()
                    stack.append(curNum * mrc)
                elif prevSign == '/':
                    mrc = stack.pop()
                    stack.append(int(mrc/ curNum))
                curNum, prevSign = 0, s[i]
                
        return sum(stack)
                    
            