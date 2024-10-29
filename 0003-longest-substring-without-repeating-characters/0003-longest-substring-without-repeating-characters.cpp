class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> i; // char: index
        int l = 0;
        int longestSubstring = 0;
        for (int r = 0; r < s.size(); r++) {
            if (i.find(s[r]) != i.end() && i[s[r]] >= l) {
                l = i[s[r]] + 1;
            }
            i[s[r]] = r;
            longestSubstring = max(longestSubstring, r-l+1);
        }
        return longestSubstring;

    }
};