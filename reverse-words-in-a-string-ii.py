class Solution:
    
    def rev(self, l, r, arr):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        
        return
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.rev(0, len(s)-1, s)
        
        start, end = 0, 0
        
        while end < len(s):
            if end == len(s)-1 and start != end:
                self.rev(start, end, s)
                end += 1
            
            elif s[end] == ' ':
                self.rev(start, end-1, s)
                start, end = end + 1, end + 1
                
            else:
                end += 1
                
        return
