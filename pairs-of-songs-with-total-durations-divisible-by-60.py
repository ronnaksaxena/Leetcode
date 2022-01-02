class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        '''
        time : count
        
        
        '''
        count = 0
        
        map = collections.defaultdict(int)
        
        for song in time:
            for prevSong, freq in map.items():
                if (song+prevSong)%60 == 0:
                    count += freq
                    
            map[song] += 1
            
        return count
