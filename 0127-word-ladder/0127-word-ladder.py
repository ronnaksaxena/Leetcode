class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        
        wordSet = set(wordList)
        q = collections.deque([beginWord])
        changes = 1 # same as depth traversed
        allLetters = [chr(i) for i in range(ord('a'), ord('z')+1)]

        while q:
            # print(changes, q)
            for _ in range(len(q)):
                curWord = q.popleft()
                if curWord == endWord:
                    return changes
                # Loop through all one change combos in curWord lowercase letters
                for letterI in range(len(curWord)):
                    for letter in allLetters:
                        newWord = curWord[:letterI] + letter + curWord[letterI+1:]
                        if newWord in wordSet:
                            q.append(newWord)
                            wordSet.remove(newWord)

            changes += 1

        return 0 # no transformations
        