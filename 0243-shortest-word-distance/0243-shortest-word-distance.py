class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        w1 = [i for i, w in enumerate(wordsDict) if w == word1]
        w2 = [i for i, w in enumerate(wordsDict) if w == word2]

        minDist = len(wordsDict)

        for i in w1:
            for j in w2:
                minDist = min(minDist, abs(i-j))
        
        return minDist
        