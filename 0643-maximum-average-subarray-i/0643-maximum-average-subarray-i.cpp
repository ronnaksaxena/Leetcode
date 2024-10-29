class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }

        int maxWindow = windowSum;
        int l = 0;
        for (int r = k; r < nums.size(); r++) {
            windowSum -= nums[l];
            l += 1;
            windowSum += nums[r];
            maxWindow = max(maxWindow, windowSum);
        }

        return (double)maxWindow / k;
    }
};