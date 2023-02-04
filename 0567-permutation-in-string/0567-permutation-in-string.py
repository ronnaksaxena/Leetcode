class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Map to hold the freq of each char in s1
        chars1 = {chr(i):0 for i in range(ord('a'), ord('z')+1)}
        for c in s1:
            chars1[c] += 1
            
        l, r = 0, 0
        while r < len(s2):
            # Could be valid permuations char
            if chars1[s2[r]] > 0:
                chars1[s2[r]] -= 1
                # Found permuation?
                if sum(chars1.values()) == 0:
                    return True
                r += 1
            # Close window and continue search
            elif l < r:
                chars1[s2[l]] += 1
                l += 1
            # No valid permutations found in prev sub
            else:
                # Need to skip this char
                r += 1
                l += 1
        return False
        
        