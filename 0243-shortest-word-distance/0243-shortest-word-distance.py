class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        indices = collections.defaultdict(list)
        for i, w in enumerate(wordsDict):
            indices[w].append(i)

        ans = len(wordsDict)
        for i1 in indices[word1]:
            for i2 in indices[word2]:
                ans = min(abs(i1-i2), ans)
        return ans
        