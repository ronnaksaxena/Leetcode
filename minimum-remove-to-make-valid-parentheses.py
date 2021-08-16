class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        forward = []
        open = 0
        
        for c in s:
            if c == '(':
                forward.append(c)
                open += 1
            elif c == ')':
                if open == 0:
                    continue
                forward.append(c)
                open -= 1
            else:
                forward.append(c)
                
        output = []
        
        for i in range(len(forward)-1,-1,-1):
            if forward[i] == '(':
                open -= 1
                if open>=0:
                    continue
            output.append(forward[i])
                
        return ''.join(output[::-1])
