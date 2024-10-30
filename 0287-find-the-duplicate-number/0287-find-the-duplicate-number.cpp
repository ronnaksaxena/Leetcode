/*
[-1,-3,-4,2,-2]
            i 
getIndex(x) => x-1

Steps:
    -loop throught nums
        - getNextIndex
        - check if elem at nextIndex is marked
            That is duplcate number
        - otherwise mark it and continue iterating
*/

void printVect(vector<int>& arr) {
    for (const int e: arr) {
        cout << e << ', ';
    }
    cout << endl;
}
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            int index = abs(nums[i]) - 1;
            if (nums[index] < 0) {
                // printVect(nums);
                return abs(nums[i]);
            }
            nums[index] *= -1;
        }
        return 0;
    }
};