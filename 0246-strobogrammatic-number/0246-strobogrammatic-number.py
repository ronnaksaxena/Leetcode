class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pair = {
            '6': '9',
            '1': '1',
            '8': '8',
            '9': '6',
            '0': '0'
        }
        l = 0
        r = len(num) - 1
        while l <= r:
            if num[l] not in pair or num[r] not in pair or num[r] != pair[num[l]]:
                return False
            l += 1
            r -= 1
            
        return True
            
        