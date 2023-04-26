class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # Not possible for odd number of elements
        if len(changed) % 2 == 1:
            return []
        output = []
        count = collections.Counter(changed)
        changed.sort(reverse=True)
        
        for half in changed:
            x = half * 2
            # special case
            if half == x:
                if count[half] >= 2:
                    output.append(half)
                    count[half] -= 2
                else:
                    continue
            elif x in count and half in count and count[x] > 0 and count[half] > 0:
                # print(x, half)
                count[x] -= 1
                count[half] -= 1
                output.append(half)
            if count[x] < 0 or count[half] < 0:
                return []

        
        return output if len(output) == (len(changed) // 2) else []
        