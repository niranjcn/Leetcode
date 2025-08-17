/**
 * Definition for a binary tree node.
 * struct TreeNode {
 * int val;
 * TreeNode *left;
 * TreeNode *right;
 * TreeNode() : val(0), left(nullptr), right(nullptr) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // 1. Base Case: Both nodes are null, so they are the same.
        if (p == nullptr && q == nullptr) return true;
        
        // 2. Base Case: One is null, the other isn't. Different structure.
        if (p == nullptr || q == nullptr) return false;
        
        // 3. Values don't match.
        if (p->val != q->val) return false;

        // 4. Recursively check left and right subtrees.
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};