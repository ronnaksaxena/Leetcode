class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        for c in s:
            stack.append(c)
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
        return ''.join(stack)
        