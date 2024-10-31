class Solution {
public:

    void printList (const vector<vector<int>> l) {
        for (vector<int> i: l) {
            cout << i[0] << " " << i[1] << " ";
        }
        cout << endl;
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> output;
        for (const vector<int>& i: intervals) {
            if (!output.empty() && output.back()[1] >= i[0]) {
                // cout << output[output.size() -1][1] << endl;
                // cout << max(output[output.size() -1][1], i[1]) << endl;
                output.back()[1] = max(output.back()[1], i[1]);
                // printList(output);
            } else {
                output.push_back(i);
            }
        }

        return output;
        
    }
};