class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        '''
        Brute Force: O(n^2)
        
        Linear backwards iteration: O(n) time O(1) spacce
        
        Forward iteration using a stack O(n) and O(n)
        maintain a strictly decreasing stack of indices with ocean view
        
        heights = [4,2,3,1]
                   i
        stack = [0, 2, 3]
        
        while stack and top of stack < current height: pop element
        push to stack
        
        '''
        
        stack = []
        for i, h in enumerate(heights):
            while stack and h >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        return stack
        