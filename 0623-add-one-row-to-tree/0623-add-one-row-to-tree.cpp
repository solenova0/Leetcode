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
 TreeNode* addOneRow(TreeNode* root, int v, int d) {
 if (d == 1) return new TreeNode(v, root, nullptr);
 queue<TreeNode*> q;
 q.emplace(root);
 while (!q.empty()) {--d;
 int sz = q.size();
 for (int s = 0; s < sz; ++s) {
 TreeNode* cur = q.front(); q.pop();
 if (d == 1) {
 cur->left = cur->left ?  new TreeNode(v, cur->left, nullptr) : new 
TreeNode(v);
 cur->right = cur->right ?  new TreeNode(v, nullptr, cur->right) : new 
TreeNode(v);
        } 
else {
 if (cur->left) q.push(cur->left);
 if (cur->right) q.push(cur->right);
        }
      }
    }
 return root;
  }
 };