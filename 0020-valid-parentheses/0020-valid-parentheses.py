class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for c in s:
            if c in '({[':
                stack.append(c)
            elif stack and stack[-1] == matches[c]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
        