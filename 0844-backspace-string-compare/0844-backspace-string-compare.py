class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack = []
        for c in s:
            if c == '#':
                if sStack:
                    sStack.pop()
            else:
                sStack.append(c)
        tStack = []
        for c in t:
            if c == '#':
                if tStack:
                    tStack.pop()
            else:
                tStack.append(c)
        return sStack == tStack
        