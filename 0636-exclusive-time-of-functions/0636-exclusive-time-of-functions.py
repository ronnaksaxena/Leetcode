class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output = [0 for _ in range(n)]
        stack = [] # [startTime, programID]
        for log in logs:
            pId, op, curTime = log.split(':')
            if op == 'start':
                if stack:
                    startTime, program = stack.pop()
                    # Calculate elapsed time
                    output[program] += (int(curTime) - startTime)
                    stack.append([int(curTime), program])
                stack.append([int(curTime), int(pId)])
            else:
                # end
                startTime, program = stack.pop()
                output[program] += (int(curTime) - startTime + 1)
                if stack:
                    stack[-1][0] = int(curTime) + 1
        return output
        
        
        
        
        
        
        
        