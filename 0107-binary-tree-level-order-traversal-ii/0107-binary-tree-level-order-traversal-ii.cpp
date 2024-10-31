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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if (!root) {
            return {};
        }
        queue<TreeNode*> q;
        vector<vector<int>> output;

        q.push(root);
        while (!q.empty()) {
            int levelCount = q.size();
            vector<int> levelNodeVals;
            for (int i = 0; i < levelCount; i++) {
                TreeNode* cur = q.front();
                q.pop();
                levelNodeVals.push_back(cur->val);
                if (cur->left != nullptr) {
                    q.push(cur->left);
                }
                if (cur->right != nullptr) {
                    q.push(cur->right);
                }
            }
            output.push_back(levelNodeVals);
        }
        reverse(output.begin(), output.end());
        return output;
        
    }
};