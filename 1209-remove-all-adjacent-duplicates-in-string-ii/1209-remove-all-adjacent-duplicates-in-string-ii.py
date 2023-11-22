class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [char, freq]
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            elif stack[-1][0] == c:
                stack[-1][1] += 1
            if stack[-1][-1] == k:
                stack.pop()
        
        return ''.join([c*f for c,f in stack])
            
        