class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = 1
        res = [str(n)]

        for i, p in enumerate(pattern):
            print(n, res)
            if p == "I":
                res.append(str(n+1))
                n += 1
            elif p == "D":
                ins = i
                # Finds the right most position to insert n+1 and maintain D
                while ins >= 0 and pattern[ins] == "D":
                    ins -= 1
                res.insert(ins+1, str(n+1))
                n += 1
        

        return "".join(res)