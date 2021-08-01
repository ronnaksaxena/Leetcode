class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
            """
            :type beginWord: str
            :type endWord: str
            :type wordList: List[str]
            :rtype: int
            """ 
            if endWord not in wordList:
                return 0
            a2w = collections.defaultdict(list)
            w2a = collections.defaultdict(list)
            n = len(wordList)
            length = len(beginWord)
            for i in range(1,length+1):
                beginWordT = beginWord[:i-1] + beginWord[i:]     
                a2w[beginWordT+str(i)].append(beginWord)
                w2a[beginWord].append(beginWordT+str(i))
                for j in range(n):
                    word = wordList[j]
                    wordT = word[:i-1] + word[i:]
                    a2w[wordT+str(i)].append(word)
                    w2a[word].append(wordT+str(i))
​
            queue = collections.deque([(beginWord,1)])
            seen = set()
