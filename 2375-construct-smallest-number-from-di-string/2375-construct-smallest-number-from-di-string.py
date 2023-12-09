class Solution:
    def smallestNumber(self, pattern: str) -> str:
        '''
        "IIIDIDDD"
            i
        curNum = 4
        num = [1,2,3]
        
        if p == I:
            add to end
        if p == D
            insertAt = len(num) - 1
            while num[insertAt]
        '''
        n = 1
        num = ['1']
        
        for i, p in enumerate(pattern):
            if p == 'I':
                n += 1
                num.append(str(n))
            else:
                ins = i
                while ins >= 0 and pattern[ins] == 'D':
                    ins -= 1
                n += 1
                # insert at ins + 1 becuase ins is at leftmost I
                num.insert(ins+1, str(n))
        return ''.join(num)
        