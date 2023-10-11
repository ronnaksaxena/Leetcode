class Solution:
    def maxValue(self, n: str, x: int) -> str:
        '''
        Time: O(logn)
        Space O(n)
        '''

        isPostive = n[0] != '-'
        insertBefore = len(n)
        if isPostive:
            for i in range(len(n)):
                if int(n[i]) < x:
                    insertBefore = i
                    break
        else:
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    insertBefore = i
                    break
        return n[:insertBefore] + str(x) + n[insertBefore:]