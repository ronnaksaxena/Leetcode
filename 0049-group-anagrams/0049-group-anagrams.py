class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = collections.defaultdict(list)

        for s in strs:
            ans[str(sorted(s))].append(s)

        return list(ans.values())