class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = collections.defaultdict(list)
        
        for word in strs:
            map[str(sorted(word))].append(word)
​
        return map.values()
