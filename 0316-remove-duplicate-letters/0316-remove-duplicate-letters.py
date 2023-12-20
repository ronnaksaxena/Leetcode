class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        "bcabc"
        
        stack => b
        
        keep stack as small as possible
        pop if curC < top of stack & top of stack appears later
        
        finalLocation = {char: last occuring index}
        
        Algo:
        finalLocation = {}
        init map:
            finalLocation[c] = i
        inStack = {}
        stack = []
        loop i, c -> s
            if c in inStack:
                continue
            while stack and stack[-1] > c and i < finalLocation[stack[-1]]:
                inStack.discard(stack.pop())
            stack.append(c)
            inStack.add(c)
        return ''.joinStack
        '''
        
        finalLoc = {}
        for i, c in enumerate(s):
            finalLoc[c] = i
        inStack = set()
        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1] > c and i < finalLoc[stack[-1]]:
                inStack.discard(stack.pop())
            stack.append(c)
            inStack.add(c)
        return ''.join(stack)
        