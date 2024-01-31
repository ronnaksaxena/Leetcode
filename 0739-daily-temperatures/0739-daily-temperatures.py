class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0 for _ in range(n)]
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                wait= i - stack[-1]
                output[stack.pop()] = wait
            stack.append(i)
        return output