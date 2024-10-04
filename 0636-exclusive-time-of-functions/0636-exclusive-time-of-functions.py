class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        '''

        duration = endTime- startTime + 1

        '''

        output = [0 for _ in range(n)]
        stack = [] # (pId, startTime)

        for log in logs:
            pId, op, timeStamp = log.split(':')
            if op == 'start':
                stack.append([int(pId),int(timeStamp)])
            else:
                _, startTime = stack.pop()
                duration = int(timeStamp) - startTime + 1
                output[int(pId)] += duration
                if stack:
                    output[stack[-1][0]] -= duration
        return output