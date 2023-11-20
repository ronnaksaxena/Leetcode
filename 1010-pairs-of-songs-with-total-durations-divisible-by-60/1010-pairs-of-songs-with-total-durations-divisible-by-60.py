class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        '''
        We would iterate through the input array time and for each element a, we want to know the number of elements b such that:
        1. b%60 == 0 and a%60 == 0
        2. b%60 == 60-a%60, if a%60 != 60
        '''
        remainders = collections.defaultdict(int)
        pairs = 0
        for t in time:
            r = (t%60)
            if r == 0:
                pairs += remainders[0]
            else:
                pairs += remainders[60-r]
            remainders[r] += 1
        return pairs