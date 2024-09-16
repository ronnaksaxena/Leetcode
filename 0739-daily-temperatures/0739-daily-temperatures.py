class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        input: int[]
        output: int[]

        Can be empty? => No
        Valid temps? => Yes
        If no future days => ans[i] = 0

        [73,74,75,71,69,72,76,73]
                              i

        stack = [6, 7]
        [1,1,4,2,1,1,0,0]

        [big -> small -> smaller] Biggest is next largest day for all elements
        To get next largest element need to maintain monotomically decreasing stack
        while top of stack temp is < current temp, 
            prevDay = stack.pop()
            ans[prevDay] = i - prevDay ==> deltas of days
        stack.append(i)

        Time: O(n)
        Spacre: O(n)
        
        '''
        stack = []
        n = len(temperatures)
        ans = [0] * n

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prevDay = stack.pop()
                ans[prevDay] = i - prevDay
            
            stack.append(i)

        return ans
        