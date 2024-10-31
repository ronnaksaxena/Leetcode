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
    int dfs(TreeNode* node, int& maxPathInTree) {
        if (!node) {
            return 0;
        }

        int left = dfs(node->left, maxPathInTree);
        int right = dfs(node->right, maxPathInTree);

        // global max path can include both sub tree but the value to return should pick one
        int nodeVal = node->val;
        // cout << nodeVal << left << right << endl;
        int maxPathToReturn = max({nodeVal, nodeVal+left, nodeVal+right});
        maxPathInTree = max({maxPathInTree, maxPathToReturn, nodeVal+left+right});
        return maxPathToReturn;

    }
    int maxPathSum(TreeNode* root) {
        int maxPathInTree = INT_MIN;
        dfs(root, maxPathInTree);
        return maxPathInTree;
    }
};