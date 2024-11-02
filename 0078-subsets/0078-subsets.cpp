class Solution {
public:
    void backtrack(vector<vector<int>>& output, int i, vector<int> curSubset, vector<int>& nums) {
        if (i == nums.size()) {
            vector<int> copy = curSubset;
            output.emplace_back(curSubset);
            return;
        }

        curSubset.emplace_back(nums[i]);
        backtrack(output, i+1, curSubset, nums);
        curSubset.pop_back();
        backtrack(output, i+1, curSubset, nums);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> output;
        int i = 0;
        vector<int> curSubset = {};
        backtrack(output, i, curSubset, nums);
        return output;
    }
};