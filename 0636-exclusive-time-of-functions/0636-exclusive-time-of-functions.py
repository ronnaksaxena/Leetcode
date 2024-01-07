class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output = [0 for _ in range(n)]
        stack = [] # [startTime, programID]
        for log in logs:
            pId, op, curTime = log.split(':')
            if op == 'start':
                stack.append([int(curTime), int(pId)])
            else:
                duration = int(curTime) - stack.pop()[0] + 1
                output[int(pId)] += duration
                if stack:
                    output[stack[-1][1]] -= duration
        return output
        
        
        
        
        
        
        
        