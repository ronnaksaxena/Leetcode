class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        '''
        Time: O(n)
        Space: O(1)
        '''
        # Edge case can't make it not a palindrome
        if len(palindrome) == 1:
            return ''
        # Find first char that is not a
        for i, c in enumerate(palindrome):
            if c == 'a':
                continue
            # Ignore middle element since it will remain a palendrome
            elif i == len(palindrome) // 2:
                continue
            # Replace with a
            return palindrome[:i] + 'a' + palindrome[i+1:]
        # All elements are a so change last one to b
        return palindrome[:-1] + 'b'
        