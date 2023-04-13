class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        tokens = path.split('/')
        
        for t in tokens:
            # go up one directory
            if not t:
                continue
            elif t == '..':
                if stack:
                    stack.pop()
            elif t == '.':
                continue
            else:
                stack.append(t)
        return '/' + '/'.join(stack)
        
        