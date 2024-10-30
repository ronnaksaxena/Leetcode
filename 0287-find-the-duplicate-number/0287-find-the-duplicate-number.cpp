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
    for (const int& e: arr) {
        cout << e << ", ";
    }
    cout << endl;
}
class Solution {
public:
    int getNextIndex(int n, vector<int>& nums) {
        return nums[n -1];
    }
    int findDuplicate(vector<int>& nums) {

        // Find the intersection point of the two runners.
        int tortoise = nums[0];
        int hare = nums[0];

        do {
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
        } while (tortoise != hare);

        // Find the "entrance" to the cycle.
        tortoise = nums[0];
        while (tortoise != hare) {
            tortoise = nums[tortoise];
            hare = nums[hare];
        }

        return hare;
    }
};