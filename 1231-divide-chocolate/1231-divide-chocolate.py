class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def canFeedEveryone(sweetLevel):
            peopleFed = 0
            currentSweetness = 0
            for s in sweetness:
                currentSweetness += s
                if currentSweetness >= sweetLevel:
                    peopleFed += 1
                    currentSweetness = 0
            return peopleFed >= (k+1)

        l = min(sweetness)
        r = sum(sweetness) // (k+1)

        while l < r:
            m = 1 + l + (r-l) // 2
            print(l, r, m)
            if canFeedEveryone(m):
                l = m
            else:
                r = m - 1
        return l
        