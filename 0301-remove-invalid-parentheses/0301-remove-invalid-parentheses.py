class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Helder to check for valid string
        def isValid(string):
            balance = 0
            for c in string:
                if c not in '()':
                    continue
                elif c == '(':
                    balance += 1
                else:
                    if balance == 0:
                        return False
                    balance -= 1
            return balance == 0
        
        # BFS to find all valid strings
        minRemovalFound = False
        output = []
        q = collections.deque([s])
        visited = {s}
        
        while q:
            cur = q.popleft()
            
            if isValid(cur):
                output.append(cur)
                minRemovalFound = True
            # No need to keep checking next level
            if minRemovalFound:
                continue
                
            # Check all removals
            for i in range(len(cur)):
                if cur[i] in '()':
                    newRemove = cur[:i] + cur[i+1:]
                    if newRemove not in visited:
                        q.append(newRemove)
                        visited.add(newRemove)
        return output if output else ['']