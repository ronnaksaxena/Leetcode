class Solution {
public:
    int bSearch(vector<int>& nums, int l, int r, int target) {
        while (l <= r) {
            int m = l + (r-l)/2;
            if (nums[m] == target) {
                return m;
            }
            else if (nums[m] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return -1;
    }
    int search(vector<int>& nums, int target) {

        // find pivot
        int l = 0, r = nums.size()-1;
        while (l < r) {
            int m = l + (r-l)/2;
            if (nums[m] > nums[r]) {
                l = m + 1;
            } else {
                r = m;
            }
        }

        int pivot = l;
        // serach left or right of pivot
        if (nums[pivot] <= target && target <= nums.back()) {
            // Serach right
            l = pivot;
            r = nums.size()-1;
            
        } else {
            // Search left
            l = 0;
            r = pivot-1;
        }

        return bSearch(nums, l, r, target);
    }
};