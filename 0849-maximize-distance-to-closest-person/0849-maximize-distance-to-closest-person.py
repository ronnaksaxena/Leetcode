class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        '''
        [1,0,0,0,1,0,1]
    l = [0,1,2,3,0,1,0]
    r = [0,3,2,1,0,1,0]

    ans = max(ans, min(left[i], right[i]))

        '''

        n = len(seats)
        left = [0] * n
        right = [0] * n

        # Forward pass to init left\
        for i in range(1, n):
            if seats[i] == 0:
                left[i] = left[i-1] + 1

        # Backward pass to init right
        for i in range(n-2, -1, -1):
            if seats[i] == 0:
                right[i] = right[i+1] + 1


        # Forward pass to calc answer
        # print(left, right)
        ans = 0
        for i, (l, r) in enumerate(zip(left, right)):
            if i == 0:
                ans = max(ans, r)
            elif i == n-1:
                ans = max(ans, l)
            else:
                ans = max(ans, min(l, r))

        return ans

        