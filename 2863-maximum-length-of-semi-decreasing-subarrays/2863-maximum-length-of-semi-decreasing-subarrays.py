class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        '''
        [7,6,1,6,10,11]

        [(11,5), (10, 4), (7, 0), (6, 1), (6)]

        

        '''
        def isSemiDecreasing(pair1, pair2):
            n1, i1 = pair1
            n2, i2 = pair2
            return n1 == n2 + 1 and i1 < i2

        nums_index = [(num, i) for i, num in enumerate(nums)]
        nums_index.sort(reverse=True)

        maxSub = 0

        for i in range(1, len(nums_index)):
            if isSemiDecreasing(nums_index[i-1], nums_index[i]):
                maxSub = max(maxSub, nums_index[i][1] - nums_index[i-1][1] + 1)

        return maxSub




        