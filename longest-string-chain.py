class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        wordSet = set(words)
        memo = {} # {word : longest chain found}
        
        def dfs(word):
            if word not in wordSet:
                return 0
            if word in memo:
                return memo[word]
            
            # Delete a char and check all combinations
            maxPath = 0
            for i in range(len(word)):
                maxPath = max(maxPath, dfs(word[:i] + word[i+1:]) + 1)
            
            memo[word] = maxPath
            return maxPath
        
        for word in words:
            dfs(word)
        
        return max(memo.values())
        
        
        
