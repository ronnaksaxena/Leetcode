#include <unordered_map>
using namespace std;
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> earliestDifference; // surplusOfOnes, index
        earliestDifference.insert({0, -1}); // edge case for subarray to begin at start
        int onesSurplus = 0;
        int longestSubarray = 0;
        for (int i = 0; i < nums.size(); i ++) {
            onesSurplus = nums[i] == 1 ? onesSurplus + 1 : onesSurplus - 1;
            // Check if we can remove a prefix array to make valid subarray
            if (earliestDifference.find(onesSurplus) != earliestDifference.end()) {
                longestSubarray = max(longestSubarray, i - earliestDifference[onesSurplus]);
            } else {
                earliestDifference[onesSurplus] = i;
            }
        }
        return longestSubarray;
    }
};