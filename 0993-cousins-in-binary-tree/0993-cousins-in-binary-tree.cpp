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
  bool isCousins(TreeNode* root, int x, int y) {
    pair<TreeNode*, int> nx = dfs(root, nullptr, x, 0);
    pair<TreeNode*, int> ny = dfs(root, nullptr, y, 0);
    return nx.first != ny.first && nx.second == ny.second;
  }
 
  pair<TreeNode*, int> dfs(TreeNode* root, TreeNode* parent, int x, int depth) {
    if (root == nullptr) return {nullptr, -1};
    if (root->val == x) return {parent, depth};
    pair<TreeNode*, int> left = dfs(root->left, root, x, depth + 1);
    pair<TreeNode*, int> right = dfs(root->right, root, x, depth + 1);
    if (left.first) return left;
    if (right.first) return right;
    return {nullptr, -1};
  }
 };