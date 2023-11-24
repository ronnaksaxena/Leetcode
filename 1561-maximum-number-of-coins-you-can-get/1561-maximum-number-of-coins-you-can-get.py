class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        '''
        piles = [2,4,1,2,7,8]
        [8,7,4,2,2,1]
           i.  i
        6-1-(2)+1 => 4 (exclusive)
        -iterate until n-1 - (n//3) + 1
        -skip by 2 and pick next highest coin since alice gets higher
        
        [9,8,7,6,5,1,2,3,4]
        [9,8,7,6,5,4,3,2,1]
                     e
        9-1-(9//3)+1 => 6
        
        8 + 6 + 4
        '''
        
        piles.sort(reverse=True)
        n = len(piles)
        end = n - (n//3)
        score = 0
        for i in range(1, end, 2):
            score += piles[i]
        return score
        
        
        
        