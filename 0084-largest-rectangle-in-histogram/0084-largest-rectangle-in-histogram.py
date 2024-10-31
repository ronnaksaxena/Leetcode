class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
    Brute force is loop through all pairs and nums[i:j] and find max rectangle area

    Would knowing the next largeset or smallest help?

    [2,1,5,6,2,3]
    1  -1

    Try all heights!
    Compute nextSmallest to left & next smallest to right

    Find are with that height
    h * (nextSmallestRight-nextSmallestLeft-1)

    Handle oob
    -1 for left
    n for right
        '''
        n = len(heights)
        
        smallestToLeft = [-1 for _ in range(n)]
        smallestToRight = [n for _ in range(n)]

        # Forward pass for left
        stack = [] # Need nondecreasing stack
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                smallestToRight[stack.pop()] = i
            stack.append(i)

        # Backward pass for right
        stack.clear()
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                smallestToLeft[stack.pop()] = i
            stack.append(i)
        stack.clear()
        # Calc max area
        maxArea = 0
        for i, h in enumerate(heights):
            # print(i, h, smallestToRight[i], smallestToLeft[i])
            maxArea = max(maxArea, h * (smallestToRight[i] - smallestToLeft[i] - 1))
        return maxArea


        