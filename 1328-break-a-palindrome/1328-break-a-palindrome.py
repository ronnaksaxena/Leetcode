class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        '''
        abba
        aaab
        '''
        # Edge case can't make it not a palindrome
        if len(palindrome) == 1:
            return ''
        
        for i, c in enumerate(palindrome):
            if c == 'a':
                continue
            elif i == len(palindrome) // 2:
                continue
            
            return palindrome[:i] + 'a' + palindrome[i+1:]
        
        return palindrome[:-1] + 'b'
        