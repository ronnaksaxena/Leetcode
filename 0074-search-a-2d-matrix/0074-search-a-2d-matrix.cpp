class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        /*
        n = rows * cols
        search space is 0 -> n

        to find elem value from pivot index
        row = i // cols
        col = i % cols

        bSearch 
        time O(logn)
        space O(1)
        */

        int rows = matrix.size(), cols = matrix[0].size();
        int n = rows * cols;

        int l = 0, r = n-1;

        while (l <= r) {
            int pivot = l + (r-l)/2;
            int elem = matrix[pivot/cols][pivot%cols];
            if (elem == target) {
                return true;
            } else if (target < elem) {
                r = pivot - 1;
            } else {
                l = pivot + 1;
            }
        }

        return false; // not found
        
    }
};