class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        chars = collections.defaultdict(list)
        
        for i in range(len(source)):
            chars[source[i]].append(i)
            
​
        idx = -1
        count = 1
        
        for i in range(len(target)):
            if target[i] not in chars:
                return -1
            idxs = chars[target[i]]
            foundValChar = False
            for j in idxs:
                if j > idx:
                    idx = j
                    foundValChar = True
                    break
                    
            if not foundValChar:
                count += 1
                idx = idxs[0]
