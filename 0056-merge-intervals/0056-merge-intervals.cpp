class Solution {
public:

    void printList (const vector<vector<int>> l) {
        for (vector<int> i: l) {
            cout << i[0] << " " << i[1] << " ";
        }
        cout << endl;
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [] (const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        vector<vector<int>> output;
        for (const vector<int>& i: intervals) {
            if (!output.empty() && output[output.size()-1][1] >= i[0]) {
                // cout << output[output.size() -1][1] << endl;
                // cout << max(output[output.size() -1][1], i[1]) << endl;
                output[output.size() -1][1] = max(output[output.size() -1][1], i[1]);
                // printList(output);
            } else {
                output.push_back(i);
            }
        }

        return output;
        
    }
};