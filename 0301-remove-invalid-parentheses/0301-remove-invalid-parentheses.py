from collections import deque

class Solution:
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Edge case empty s
        if len(s) == 0:
            return [""]
        
        # helper to check if the expression is valid
        def isValid(expr):
            count = 0
            for ch in expr:
                if ch not in '()':
                    continue
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0


        visited = {s}
        queue = deque([s])
        minRemovalFound = False
        output = []

        while queue:
            expr = queue.popleft()

            if isValid(expr):
                output.append(expr)
                minRemovalFound = True

            if minRemovalFound:
                continue
                
            # Search all removals to see if you van find valid parenthesis
            for i in range(len(expr)):
                # Can't remove letters
                if expr[i] not in '()':
                    continue

                candidate = expr[:i] + expr[i+1:] 
                if candidate not in visited:
                    queue.append(candidate)
                    visited.add(candidate)
                    
        # If not candidates found return empty string
        return output if output else [""]