class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        res = [c for c in s]
        l, r = 0, len(res)-1
        
        while l < r:
            # Ignore non vowels
            while l <= r and res[l] not in vowels:
                l += 1
            while l <= r and res[r] not in vowels:
                r -= 1
            # Finished rev
            if l >= r:
                break
            # swap
            res[r], res[l] = res[l], res[r]
            l += 1
            r -= 1
            
        return ''.join(res)
        