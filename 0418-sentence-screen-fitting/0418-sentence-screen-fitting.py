class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)
        # i is index of sentence
        # returns (times sentence completed, index of sentence)
        @cache
        def dp(i):
            completions = 0
            c = 0
            # See how many words can fit in this col
            while c + len(sentence[i]) <= cols:
                c += len(sentence[i]) + 1
                i += 1
                if i == n:
                    completions += 1
                    i = 0
            return completions, i
        
        ans = 0
        wordIndex = 0
        # Call for number of rows given
        for _ in range(rows):
            ans += dp(wordIndex)[0]
            wordIndex = dp(wordIndex)[1]
            
        return ans
            
            
        