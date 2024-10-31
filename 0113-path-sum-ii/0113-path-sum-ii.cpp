/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void dfs(TreeNode* node, int& sumSoFar, int targetSum, vector<int>& pathSoFar, vector<vector<int>>& output) {
        // cout << node->val << endl;
        pathSoFar.push_back(node->val);
        sumSoFar += node->val;
        if (!node->left && !node->right && sumSoFar == targetSum) {
            vector<int> pathCopy = pathSoFar;
            output.push_back(pathCopy);
        }
        if (node->left) {
            dfs(node->left, sumSoFar, targetSum, pathSoFar, output);
        }
        if (node->right) {
            dfs(node->right, sumSoFar, targetSum, pathSoFar, output);
        }
        // Remove this node for next path
        pathSoFar.pop_back();
        sumSoFar -= node->val;
        return;
    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        if (!root) {
            return {};
        }
        vector<vector<int>> output;
        int sumSoFar = 0;
        vector<int> path = {};
        dfs(root, sumSoFar, targetSum, path, output);
        return output;
    }
};