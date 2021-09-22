class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, cur = [], ''
        path += '/'
        for c in path:
            if c == '/':
                if cur == '..':
                    if stack: stack.pop()
                elif cur != '.' and cur != '':
                    print(cur,'here')
                    stack.append(cur)
                cur = ''
            else:
                cur += c
        
        return '/' + '/'.join(stack)
        
