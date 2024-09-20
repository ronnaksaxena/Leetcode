class Solution:
    def reverseParentheses(self, s: str) -> str:
        '''
        input: string
        output: string

        - s can be empty
        - valid input
        - only letters

        ex. "(ed(et(oc))el)"
                         i
        stack = [[e, d, co, t, e, e, l]]
        [e, t, co]
        le e t co d e

        Intution: stack for nests
        - if ( add new chunk by [] to stack
        - if )
            - pop chunk from stack
            - helper fn to reverse character
            - push reversed output onto last chunk in stack if empty push onto stack
        - if letter add to last chunk in stack

        Time: O(n^2) iterate throught elements and reverse element
        Space: O(n) for stack
        
        '''
        def helper(i, s):
            def reverse(arr):
                return ''.join(arr)[::-1]
            stack = []

            while i < len(s):
                if s[i] == '(':
                    stack.append([])
                elif s[i] == ')':
                    chunk = stack.pop()
                    if stack:
                        stack[-1].append(reverse(chunk))
                    # Reversed all parenthesis
                    else:
                        return i+ 1, reverse(chunk)
                else:
                    stack[-1].append(s[i])
                
                i += 1
            return stack.pop()

        i = 0
        ans = []
        while i < len(s):
            if s[i].isalpha():
                ans.append(s[i])
                i += 1
            elif s[i] == '(':
                i, chunk = helper(i, s)
                ans.append(chunk)
        return ''.join(ans)

