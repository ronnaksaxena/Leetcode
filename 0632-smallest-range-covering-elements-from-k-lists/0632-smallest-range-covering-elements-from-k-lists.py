class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        '''
        smallest range is min(b-a) for range [a,b] if there is a tie; range1[0] < range2[0] menas range1 smaller

        [4,10,15,24,26]
        [0,9,12,20]
        [5,18,22,30]
        ->
        use each list is already sorted
        start with range [0,5]
        can increase L or decrease H
            - since the arrays are already sort we should increase L and see if we can find a smaller range
            - since we traverse thise way if there is a tie we know our current range is smaller

        STOP iteration at last elem of a arr since no more elements will be larger than min and have an element in all arrays

        Time: O(logk * n) where k is # of lists and n is total elements
        Space: O(k)
        '''

        k = len(nums) # number of lists
        pq = [] # (elem, list index, element index)
        mmax = float('-inf')

        # init pq
        for i in range(k):
            heapq.heappush(pq, (nums[i][0], i, 0))
            mmax = max(mmax, nums[i][0])
        
        # Window is [top of pq, mmax]
        ans = [pq[0][0], mmax]

        while True:
            _, listIndex, numIndex = heapq.heappop(pq)
            # Terminate
            # No greater element will have an element in all lists
            if numIndex == len(nums[listIndex]) -1:
                return ans

            # Compare to nextNum bc our old range included nums[listIndex][numIndex] and want to check if we can get a smaller one by adding ums[listIndex][numIndex+1]
            nextNum = nums[listIndex][numIndex+1]
            mmax = max(mmax, nextNum)
            # Push next index onto pq
            # Need to do this before updating answer to maintain state of range
            heapq.heappush(pq, (nextNum, listIndex, numIndex+1))
            # update answer
            if (mmax - pq[0][0]) < (ans[1]-ans[0]):
                ans = [pq[0][0], mmax]


        return ans

        