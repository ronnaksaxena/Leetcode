class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        p = 0
        count = 1
        curC = chars[0]
        for c in chars[1:]:
            if c != curC:
                if count == 1:
                    chars[p] = curC
                    p += 1
                else:
                    chars[p] = curC
                    p += 1
                    for d in [d for d in str(count)]:
                        chars[p] = d
                        p += 1
                count = 1
            else:
                count += 1
            curC = c
        if count == 1:
            chars[p] = curC
            p += 1
        else:
            chars[p] = curC
            p += 1
            for d in [d for d in str(count)]:
                chars[p] = d
                p += 1
        return p
                
        