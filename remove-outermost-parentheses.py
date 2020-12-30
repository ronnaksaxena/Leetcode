class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        if not S:
            return ""
        openIdx = 0
        closeIdx = 0
        cur = 0
        stack = []
        while cur<len(S):
            if not stack and S[cur]=='(':
                stack.append('(')
                openIdx = cur
                cur += 1
            elif len(stack)==1 and S[cur]==')':
                stack.pop()
                closeIdx = cur
                S = S[:openIdx]+S[openIdx+1:closeIdx]+S[closeIdx+1:]
                cur -= 1
            elif S[cur]=='(':
                stack.append('(')
                cur += 1
            elif S[cur]==')':
                stack.pop()
                cur += 1
        return S
