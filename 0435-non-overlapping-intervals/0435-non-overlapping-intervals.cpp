class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) {
            return 0;
        }
        int count = 0;
        sort(intervals.begin(), intervals.end());
        int lastIntervalEnd = intervals[0][1];

        for (int i = 1; i < intervals.size(); i++) {
            if (lastIntervalEnd > intervals[i][0]) {
                // cout << lastIntervalEnd << intervals[i][0] << endl;
                count++;
                lastIntervalEnd = min(lastIntervalEnd, intervals[i][1]);
            } else {
                lastIntervalEnd = intervals[i][1];
            }
        }

        return count;
        
    }
};