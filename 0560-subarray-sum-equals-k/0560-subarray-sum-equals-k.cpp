/*
    [1,2,3], k = 3
   0 1 3 3
   0: 1
   1: 1
   3: 1
   6: 1

   if curSum - k in map
    ans += map[curSum-k]
map[curSum] += 1
*/

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> pSums; // sum: count
        pSums[0] = 1;
        int ans = 0;
        int curSum = 0;

        for (int i = 0; i < nums.size(); i++) {
            curSum += nums[i];
            int difference = curSum-k;
            if (pSums.find(difference) != pSums.end()) {
                ans += pSums[difference];
            }

            // Update map
            if (pSums.find(curSum) != pSums.end()) {
                pSums[curSum] += 1;
            } else {
                pSums[curSum] = 1;
            }
        }

        return ans;
    }
};