class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        '''
        Qs:
        - diff is smaller, if tie first element <
        - 105 <= nums[i][j] <= 105
        - nums sorted and can be duplicates
        - output: [start, end] inclusive

        nums = 
        [[4,10,15,24,26],
         [0,9,12,20],
         [5,18,22,30]]

        Brute Force: NLogN * k where n is total elements in list and k is # of lists
        - put all elements into a list
        - sort the list
        - [l ..... r]
            check that every list have an element in the range
            terminate the loop

        Priority Queue
        nums = 
        [[4,10,15,24,26],
         [0,9,12,20],
                  stop
         [5,18,22,30]]

        (element Value, listIndex, numIndex)
        pq = [ 5, 10, 9] => minHeap of size K
        max = 10
        L increases
        ans = [newL, max] => [0, 5]

        Algo:
        1. populate my initial pq with first elements
        2. loop thorught q
            - pop smallest element
            - check if new range is smaller
                - terminate if we've reached the end of a list
            - push next element in that list onto priority

        Time logK * N where K is # of lists of lists and N is total elements
        Space: O(K) will never have more than K elements in pq


        '''

        def isRangeSamller(range1, currentAns):
            # Note that currentAns[0] < range[0]
            print(range1, currentAns)
            return (range1[1]-range1[0]) < (currentAns[1] - currentAns[0])

        pq = []
        rangeMax = float('-inf')

        for listIndex, val in enumerate(nums):
            heapq.heappush(pq, (val[0], listIndex, 0))
            rangeMax = max(rangeMax, val[0])
        ans = [pq[0][0], rangeMax]
        while pq:
            currentElem, listIndex, numIndex = heapq.heappop(pq)

            # Out of elements in list
            if numIndex == len(nums[listIndex]) - 1:
                return ans
            
            nextElem = nums[listIndex][numIndex+1]
            rangeMax = max(rangeMax, nextElem)

            heapq.heappush(pq, (nextElem, listIndex, numIndex+1))
            
            if isRangeSamller([pq[0][0], rangeMax], ans):
                ans = [pq[0][0], rangeMax]

            

        return ans

        