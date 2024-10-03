class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        '''
        Clarifying Questions:
        - input: String, output: int (min flips needed)
        - valid input, no memory constraints, not empty string
        - can be all zeroes or all ones, otherwise zeroes followed by ones

        EDGE CASES:
            - s with lenght of 1: return 0
            - s that we need to flip entirely to 0s or 1s
            [0,0,0,0]
        

        "00011000" -> 00000000

        [left] [right]
         min(1) min(0)

         "010110"
                ^
                |
    [left1s -> i) [right0 -> n-1]
    - come to back to off by 1

    operations = left1s + right0s => flipsNeeded at this current partition
    ans => min(ans, currentOperationsNeeded)

         - evaluate edge cases
         -

         idea: prefixSum
         precompute sum of 1s and sum of 0s

         Algo:
         - init our prefix sums arrays
         - iterate throught the input and calculate operations needed for each partition
            (CAREFUL of off by 1)
         - return number of flips for optimal partition

         Time: O(n)
         Space: O(n)

        '''

        n = len(s)
        if n <= 1:
            return 0
        
        # init
        '''
        x 1s in [0->i]
        (i+1) - x => 0
        '''
        prefix1 = [0] * n
        prefix0 = [0] * n
        if s[0] == '1':
            prefix1[0] = 1
        else:
            prefix0[0] = 1

        for i in range(1, n):
            if s[i] == '1':
                prefix1[i] = prefix1[i-1] + 1
                prefix0[i] = prefix0[i-1]
            else:
                prefix0[i] = prefix0[i-1] + 1
                prefix1[i] = prefix1[i-1]

        # EDGE cases if all 0s or all 1s
        ans = min(prefix1[-1], prefix0[-1])

        for i in range(1, n): # double check off by 1
            left1 = prefix1[i-1]
            right0 = prefix0[-1] - prefix0[i-1]
            ans = min(ans, left1+right0)

        return ans

        '''
        "010110"
              
        left = [0, n-2]
        rihgt = [n-1, n-1]
        p0 = [1, 1, 2, 2, 2, 3]
        p1 = [0, 1, 1, 2, 3, 3]


        '''


        