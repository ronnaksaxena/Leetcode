class Solution {
public:
    vector<string> copyBoard(vector<vector<string>> board) {
        vector<string> copy;
        for (vector<string>& row: board) {
            string s = "";
            for (string& c: row) {
                s += c;
            }
            copy.push_back(s);
        }
        return copy;
    }
    bool canPlace(unordered_map<string, unordered_set<int>>& used, int r, int c) {
        int d = r-c;
        int rd = r+c;
        /*
        d: (r-c) top left to bottom right;
        Primary Diagonal Index	Cells
        -3	(3, 0)
        -2	(2, 0), (3, 1)
        -1	(1, 0), (2, 1), (3, 2)
        0	(0, 0), (1, 1), (2, 2), (3, 3)
        1	(0, 1), (1, 2), (2, 3)
        2	(0, 2), (1, 3)
        3	(0, 3)

        rd: (r+c) top right to bottom left
        Secondary Diagonal Index	Cells
        0	(0, 0)
        1	(0, 1), (1, 0)
        2	(0, 2), (1, 1), (2, 0)
        3	(0, 3), (1, 2), (2, 1), (3, 0)
        4	(1, 3), (2, 2), (3, 1)
        5	(2, 3), (3, 2)
        6	(3, 3)
        */
        return !(used["r"].find(r) != used["r"].end() || used["c"].find(c) != used["c"].end() || used["d"].find(d) != used["d"].end() || used["rd"].find(rd) != used["rd"].end());
    }
    void place(unordered_map<string, unordered_set<int>>& used, vector<vector<string>>& board, int r, int c) {
        used["r"].insert(r);
        used["c"].insert(c);
        used["d"].insert(r-c);
        used["rd"].insert(r+c);
        board[r][c] = "Q";
    }
    void unplace(unordered_map<string, unordered_set<int>>& used, vector<vector<string>>& board, int r, int c) {
        used["r"].erase(r);
        used["c"].erase(c);
        used["d"].erase(r-c);
        used["rd"].erase(r+c);
        board[r][c] = ".";
    }

    void backtrack(vector<vector<string>>& output, vector<vector<string>>& board, unordered_map<string, unordered_set<int>>& used, int r, int n) {
        if (r == n) {
            vector<string> copy = copyBoard(board);
            output.push_back(copy);
            return;
        }

        int totalCols = n;
        for (int c = 0; c < totalCols; c++) {
            if (canPlace(used, r, c)) {
                place(used, board, r, c);
                backtrack(output, board, used, r+1, n);
                unplace(used, board, r, c);
            }
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> output;
        vector<vector<string>> board(n, vector<string>(n, "."));
        unordered_map<string, unordered_set<int>> usedCols = {
            {"r", {}},
            {"c", {}},
            {"d", {}},
            {"rd", {}},
        };
        backtrack(output, board, usedCols, 0, n);
        return output;
    }
};