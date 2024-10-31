class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {

        vector<vector<int>> output;
        int i = 0;

        while (i < intervals.size() and intervals[i][0] < newInterval[0]) {
            output.emplace_back(intervals[i]);
            i++;
        }

        // Insert newInternval and check if merge
        if (!output.empty() and output.back()[1] >= newInterval[0]) {
            output.back()[1] = max(output.back()[1], newInterval[1]);
        } else {
            output.emplace_back(newInterval);
        }

        // Add remaining intervals
        while (i < intervals.size()) {
            if (output.back()[1] >= intervals[i][0]) {
                output.back()[1] = max(output.back()[1], intervals[i][1]);
            } else {
                output.emplace_back(intervals[i]);
            }
            i++;
        }
        
        return output;
    }
};