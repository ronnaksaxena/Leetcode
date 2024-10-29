#include <vector>
using namespace std;

class NumArray {
private:
    vector<int> prefixSum;

public:
    NumArray(vector<int>& nums) {
        prefixSum.resize(nums.size());
        int curSum = 0;
        for (int i = 0; i < prefixSum.size(); i++) {
            curSum += nums[i];
            prefixSum[i] = curSum;
        }
    }
    
    int sumRange(int left, int right) {
        return (left == 0 ? prefixSum[right] : prefixSum[right] - prefixSum[left-1]);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */