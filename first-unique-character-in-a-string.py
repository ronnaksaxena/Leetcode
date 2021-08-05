class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = collections.Counter(s)
        
        lowChar = min(map, key=map.get)
        
        return s.find(lowChar) if map[lowChar] == 1 else -1
