class Solution {
public:
    int getNextNum(int n) {
        string digits = to_string(n);
        int result = 0;
        for (const char& c: digits) {
            result += pow(c - '0',2);
        }
        return result;
    }
    bool isHappy(int n) {
        if (n == 1) {
            return true;
        }
        int slow = n;
        int fast = n;

        while (fast != 1 && getNextNum(fast) != 1) {
            slow = getNextNum(slow);
            fast = getNextNum(getNextNum(fast));

            // cout << "slow " << slow << " fast " << fast << endl;

            if (slow == fast) {
                return false;
            }
        }

        return true;
    }
};