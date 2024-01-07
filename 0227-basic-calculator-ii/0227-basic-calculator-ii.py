class Solution:
    def calculate(self, s: str) -> int:
        # Have prevSign as + initially to add 0 to first term
        curNum, prevSign = 0, '+'
        stack = []
        s = s.replace(' ', '') # Remove whitestpace
        
        for i in range(len(s)):
            
            if s[i].isnumeric():
                curNum = curNum*10 + int(s[i])
                
            # if not elif becuase last char could be num
            if s[i] in '+-/*' or i == len(s)-1:
                if prevSign == '+':
                    stack.append(curNum)
                elif prevSign == '-':
                    stack.append(curNum * -1)
                elif prevSign == '*':
                    # mrc is Most Recent Calculation
                    mrc = stack.pop()
                    stack.append(curNum * mrc)
                elif prevSign == '/':
                    mrc = stack.pop()
                    # int() to handle truncating down negative values
                    stack.append(int(mrc / curNum))
                curNum, prevSign = 0, s[i]
                
        return sum(stack)
                    
            