class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        '''
        Questions:
        - input: list[int], k: int
        - output: int => MAX piece you can eat
        - k + 1 subarrarys needed
        - length of sweetness <= (k+1)
        - sweetness are positive ints
        - no memory constraints


        EDGE CASE:
            - len sweetnesss == k+t => return min(sweetness)
            - k == 0 => return sum(sweetness)

        BRUTE FORCE: in k + 1 nested loops find every partition of sweetness array and return max(min subarray sum)

        O(n^k)

        Idea: look for optimal sweetness level
        - if partition into k+1 subarrays each subararray sum >= sweetness level
        -> Binary Search
            - search space: [min(sweetness), sum(sweetness)]
            helper fn(sweetnessLevel) => boolean
                -> returns True if everyone can achieve these sweeetness level

        What is the search space?
        How can we reduce the search space?
        When can we return the result?

        ALGO:
        l, r = [min(sweetness), sum(sweetness)]
        while l < r
            sweetlevel = m
            if validLevel(sweetlevel):
                l = m
            else:
                r = m - 1
        return l

        [1,2,3,4,5,6,7,8,9], k = 5

        1. l = 1, r = 47
            m = 24
        2. l = 1, r = 23
            m = 12
        3. l = 1, r = 11
            m = 6
        4. l = 6, r == 11
            m = 8
        5. l = 6, r = 8
            m = 7
        6. l = 6, r = 6

        Time: O(log Sum(sweetness))
        Space: O(1)

        '''

        def validSweetnessLevel(sweetLevel):
            people = 0
            currSweetness = 0
            for s in sweetness:
                currSweetness += s
                if currSweetness >= sweetLevel:
                    people += 1
                    currSweetness = 0
                if people == (k+1):
                    break
            return people >= (k+1)

        # edge cases
        if len(sweetness) == k+1:
            return min(sweetness)
        if k == 0:
            return sum(sweetness)

        l = min(sweetness)
        r = sum(sweetness)

        while l < r:
            m = l + (r-l)//2
            if validSweetnessLevel(m):
                l = m if m != l else l + 1
            else:
                r = m - 1
        
        return l
        