class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(arr)
        ranks = {} # Value: Rank
        rank = 1
        i = 0
        while i < len(sortedArr):
            ranks[sortedArr[i]] = rank
            rank += 1
            i += 1
            while i < len(sortedArr) and sortedArr[i] == sortedArr[i-1]:
                i += 1
        
        output = [0 for _ in range(len(arr))]
        for j in range(len(arr)):
            output[j] = ranks[arr[j]]
        
        return output
        
            
        