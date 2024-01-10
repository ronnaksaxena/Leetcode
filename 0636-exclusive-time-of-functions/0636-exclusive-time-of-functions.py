class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output = [0 for _ in range(n)]
        stack = [] # [pId, time]
        
        for log in logs:
            pId, operation, timestamp = log.split(':')
            pId = int(pId)
            timestamp = int(timestamp)
            
            if operation == 'start':
                stack.append([pId, timestamp])
            else:
                p, t = stack.pop()
                duration = timestamp - t + 1
                output[p] += duration
                # If program was halted decriment by this program duration
                if stack:
                    output[stack[-1][0]] -= duration
            
        return output
        