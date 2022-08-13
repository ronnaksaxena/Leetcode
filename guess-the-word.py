# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
​
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def mostCommonWord():
            # Store freq of char in each position
            # [0] ...[i][all chars frequence] ...[5]
            count = [[0] * 26 for i in range(6)]
            # First loop calculates frequency of all remaining word choices
            for word in wordlist:
                for i, c in enumerate(word):
                    count[i][ord(c)-ord('a')] += 1
            
            # Second loop find most common word
            maxScore = 0
            msc = ''
            for word in wordlist:
                curScore = 0
                for i, c in enumerate(word):
                    curScore += count[i][ord(c)-ord('a')]
                if curScore > maxScore:
                    maxScore = curScore
                    msc = word
            
            return msc
            
        def pairsFound(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))
        
        def filterList(word, numMatches):
            newList = []
            for w in wordlist:
                if pairsFound(word, w) == numMatches:
                    newList.append(w)
            return newList
        
        
        while wordlist:
            # Find MSC that would remove max number of false candidates
            guessWord = mostCommonWord()
            matches = master.guess(guessWord)
            # Found secret word
            if matches == 6:
                return
            
            # Filter list by removing all invalid candidates
            wordlist = filterList(guessWord, matches)
        
