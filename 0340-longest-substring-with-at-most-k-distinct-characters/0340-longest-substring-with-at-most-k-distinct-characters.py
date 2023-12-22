class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, n: int) -> int:
        # longest substring
        longestSubstring = 0
          # Will store all distinct values in window
        counter = collections.Counter()

          # SLiding window
        for index in range(len(s)):
            # For how many of these values 
            counter[s[index]] += 1

            # If our dict is less than or equal to n distanc values
            # {"a": 1, "b": 2} len = 2 abccd
            if len(counter) <= n:
                longestSubstring += 1
            else: # We have n + 1 distanct values, we need to 
                counter[s[index - longestSubstring]] -= 1 # Remove leftmost
                # We want to remove the leftmost key from sliding window
                if counter[s[index - longestSubstring]] == 0:
                    del counter[s[index - longestSubstring]]
        return longestSubstring
        