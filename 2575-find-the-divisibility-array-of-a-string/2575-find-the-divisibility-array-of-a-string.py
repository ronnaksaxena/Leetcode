class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        divArr = [0 for _ in range(n)]
        digits = [int(d) for d in word]
        runningSum = 0
        
        for i, n in enumerate(digits):
            runningSum = runningSum * 10 + n
            if runningSum % m == 0:
                divArr[i] = 1
            runningSum %= m
                
        return divArr
            
        