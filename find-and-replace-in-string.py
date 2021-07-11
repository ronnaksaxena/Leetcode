class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = []
        map = collections.defaultdict()
        
        for idx,src,targ in zip(indices,sources,targets):
            map[idx] = (src,targ)
        
        i = 0
        while i < len(s):
            if i in map.keys():
                src, targ = map[i]
                if s[i:].find(src) == 0:
                    ans.append(targ)
                    i += len(src)
                else:
                    ans.append(s[i])
                    i += 1
            else:
                ans.append(s[i])
                i += 1
        return ''.join(ans)
        
