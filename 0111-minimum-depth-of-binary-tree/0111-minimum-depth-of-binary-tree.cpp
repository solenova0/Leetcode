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
  int minDepth(TreeNode* root) {
    if (root == nullptr) return 0;
    stack<pair<TreeNode*, int>> st;
    st.emplace(root, 1);
    int min_depth = numeric_limits<int>::max();
    while (!st.empty()) {
      pair<TreeNode*, int> cur = st.top(); st.pop();
      if (cur.first->left == nullptr && cur.first->right == nullptr) min_depth = 
min(min_depth, cur.second);
      if (cur.first->left != nullptr) st.emplace(cur.first->left, cur.second + 
1);
      if (cur.first->right != nullptr) st.emplace(cur.first->right, cur.second + 
1);
    }
    return min_depth;
  }
 };