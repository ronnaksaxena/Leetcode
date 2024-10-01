class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        '''
        "00011000"
              r
             l

        How many 1s in l? 2
        How many 0s in r? 3

        total 5 flips?

        flips = left1 + right0
        
        prefixSum 1
        prefixSum 0

        prefixSum1[index] + prefixSum2[index+1]

        find min of adding these

        time: O(N)
        Space: O(N)
        '''
        n = len(s)
        pSum1 = [0] * n
        pSum0 = [0] * n
        oneCount = 0
        zeroCount = 0

        for i in range(n):
            if s[i] == '1':
                oneCount += 1
            else:
                zeroCount += 1
            pSum1[i] = oneCount
            pSum0[i] = zeroCount

        # Compare all 1s or all 0s
        ans = min(pSum1[-1], pSum0[-1])

        for split in range(n):
            left1s = pSum1[split-1]
            right0s = pSum0[-1] - (pSum0[split-1] if split > 0 else 0)
            ans = min(ans, left1s + right0s)

        return ans

        