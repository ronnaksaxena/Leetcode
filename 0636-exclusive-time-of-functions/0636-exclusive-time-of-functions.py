class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output = [0 for _ in range(n)]
        stack = [] # [(fnID, startTime)]
        
        for l in logs:
            fnID, operation, timeStamp = l.split(':')
            fnID = int(fnID)
            timeStamp = int(timeStamp)
            if operation == 'start':
                stack.append((fnID, timeStamp))
            else:
                _, startTime = stack.pop()
                duration = timeStamp - startTime + 1 # to include current time
                output[fnID] += duration
                # Decriment paused fn times
                if stack:
                    output[stack[-1][0]] -= duration
        return output
                
            
        