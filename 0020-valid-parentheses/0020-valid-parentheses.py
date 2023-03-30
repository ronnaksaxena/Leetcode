class Solution:
    def isValid(self, s: str) -> bool:
        
        pairings = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = []
        for c in s:
            
            if c in pairings:
                if not stack or stack[-1] != pairings[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0
        