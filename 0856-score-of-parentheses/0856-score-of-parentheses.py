class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        '''
        "(())"
            i
        [2]

        '''

        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                innerScore = stack.pop()
                stack[-1] += (2*innerScore if innerScore > 0 else 1)
        return stack.pop()
        