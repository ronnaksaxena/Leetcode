class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        - only deletions
        - lowercase english letters and ()
        - non empty string
        
        "lee(t(c)o)de)(((" => "lee(t(c)o)de"
                      i
        stack = [l, e, e, (, t, (, c, ), o, ), d, e, (, (, (]
        balance = 3
        
        output = []
        
        
        
        - each opening must have matching closing
        
        Ideas: Stack to hold letters and valid brackets
        - init stack
        - push if letter
        - if opening parenthesis inc balance
        - only add closing parenthis if balance > 0
            - dec balance
        - pop from stack and add to output
            - do not include if ( and balance > 0
        
        Time: O(n) 2 traversals through string
        Space: O(n) for stack
        '''
        
        stack = []
        balance = 0
        # First loop adds all valid closing parenthsis
        for c in s:
            if c.isalpha():
                stack.append(c)
            elif c == '(':
                stack.append(c)
                balance += 1
            else:
                # closing parenthsis
                if balance > 0:
                    stack.append(c)
                    balance -= 1
        output = []
        # Second loop discard all invalid opening parenthesis
        while stack:
            if stack[-1].isalpha() or stack[-1] == ')':
                output.append(stack.pop())
            else:
                # Opening parenthesis
                if balance > 0:
                    stack.pop()
                    balance -= 1
                else:
                    output.append(stack.pop())
        return ''.join(output[::-1])
                
                    
                
                
                
                
                
                