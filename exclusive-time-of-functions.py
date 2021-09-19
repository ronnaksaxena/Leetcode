class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        stack = []
        output = [0 for _ in range(n)]
        
        for log in logs:
            parts = log.split(':')
            id, call, time = int(parts[0]), parts[1], int(parts[2])
            
            if call == 'start':
                stack.append([id, time])
            else:
                cur_fn, cur_time = stack.pop()
                dur = time-cur_time+1
                output[cur_fn] += dur
                
                if stack:
                    output[stack[-1][0]] -= dur
                    
        return output
