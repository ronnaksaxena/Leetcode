class Solution {
public:
    void printList(vector<int>& l) {
        for (int n: l) {
            cout << n << " ";
        }
        cout << endl;
    }
    void swap(vector<int>& nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    void backtrack(vector<vector<int>>& output, int i, vector<int>& nums) {
        if (i == nums.size()) {
            vector<int> permutationCopy = nums;
            // printList(permutationCopy);
            output.push_back(permutationCopy);
            return;
        }

        for (int j = i; j < nums.size(); j++) {
            swap(nums, i, j);
            backtrack(output, i+1, nums);
            swap(nums, i, j);
        }

    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> output;
        int i = 0;
        backtrack(output, i, nums);
        return output;
    }
};