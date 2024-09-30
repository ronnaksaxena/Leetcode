class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        '''
        -condition(x) is x a workable value?
            - can cut into k+1 pieace and each piece sweetness >= x

        - search space
            left is min(sweetness) can't have a chunk < min piece
            right is sum(sweetness) // people or k + 1
                if everyone gets a piece this is largest I can get myself
        
        return: left

        '''

        def isSweetEnough(sweetLevel):
            peopleWithChocolate = 0
            curSweet = 0
            for s in sweetness:
                curSweet += s
                if curSweet >= sweetLevel:
                    peopleWithChocolate += 1
                    curSweet = 0
            return peopleWithChocolate >= k + 1

        left = min(sweetness)
        right = sum(sweetness) // (k + 1)

        while left < right:
            mid = 1 + left + (right - left) // 2
            if isSweetEnough(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
        