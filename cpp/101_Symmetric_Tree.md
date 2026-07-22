# ↔️ LeetCode 101: Symmetric Tree

![LeetCode](https://img.shields.io/badge/LeetCode-101-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style-for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Tree%2C%20DFS%2C%20BFS-brightgreen?style-for-the-badge)

---

## 📘 Problem Statement

> Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

---

## 📥 Example Inputs

### ✅ Example 1:

```cpp
Input: root = [1,2,2,3,4,4,3]
Output: true
✅ Example 2:
C++

Input: root = [1,2,2,null,3,null,3]
Output: false
📌 Constraints
The number of nodes in the tree is in the range [1, 1000].

-100 <= Node.val <= 100.

💡 Pattern & Approach
This problem requires comparing two subtrees to see if they are mirror images of each other. This is a classic tree traversal problem that can be solved recursively or iteratively.

Depth-First Search (DFS) (recursive, using a helper function)

Breadth-First Search (BFS) (iterative, using a queue)

🔍 The Logic
🔹 Approach 1: Depth-First Search (DFS - Recursive)
The core idea is that a tree is symmetric if its left subtree is a mirror image of its right subtree. We can write a helper function isMirror(t1, t2) that checks this property.

Main Function

The entry point isSymmetric(root) simply calls the helper on the root's two children: isMirror(root->left, root->right).

Base Cases (in isMirror)

If both nodes t1 and t2 are null, they are symmetric. Return true.

If only one is null or if their values differ, they are not symmetric. Return false.

Recursive Step (The "Cross-Check")

The key to symmetry is that the left subtree of t1 must mirror the right subtree of t2.

AND the right subtree of t1 must mirror the left subtree of t2.

Return isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left).

🔹 Approach 2: Breadth-First Search (BFS - Iterative)
This approach compares the tree level by level, ensuring that each level is a palindrome.

Initialize

Create a queue and push the root's left and right children. You push two nodes at a time to be compared.

Iterate and Compare

While the queue is not empty, dequeue two nodes, t1 and t2.

Validate Nodes

Check the pair: if both are null, continue. If only one is null or their values differ, return false.

Enqueue Children (in Mirrored Order)

To maintain the symmetry check, push the children of t1 and t2 in a specific, mirrored order:

t1->left and t2->right

t1->right and t2->left

Return Result

If the queue empties without returning false, the tree is symmetric.

🏃‍♂️ Dry Run Example (DFS)
Given:
root = [1,2,2,null,3,null,3] (The false case)

isSymmetric(root(1))
│
└── calls isMirror(root->left(2), root->right(2))
    │
    ├── Checks: Nodes are valid. Values are equal (2 == 2). OK.
    │
    ├── isMirror(2->left(null), 2->right(3))
    │   │
    │   └── Checks: One node is null, the other is not.
    │   └── returns false
    │
    └── The first recursive "cross-check" returned false.
        The overall '&&' expression becomes false.

→ Final result is false.
💻 C++ Code
Approach 1: Recursive DFS

C++

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 * int val;
 * TreeNode *left;
 * TreeNode *right;
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        return isMirror(root->left, root->right);
    }

    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // Both subtrees are empty, they are mirrors.
        if (!t1 && !t2) return true;
        // One is empty, the other isn't. Not mirrors.
        if (!t1 || !t2) return false;
        // Values don't match. Not mirrors.
        if (t1->val != t2->val) return false;

        // Recursively check the outer children (left-right) and inner children (right-left).
        return isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left);
    }
};
Approach 2: Iterative BFS

C++

#include <queue>

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;

        std::queue<TreeNode*> q;
        q.push(root->left);
        q.push(root->right);

        while (!q.empty()) {
            TreeNode* t1 = q.front();
            q.pop();
            TreeNode* t2 = q.front();
            q.pop();

            if (!t1 && !t2) continue;
            if (!t1 || !t2 || t1->val != t2->val) {
                return false;
            }

            // Enqueue in mirrored order
            q.push(t1->left);
            q.push(t2->right);
            q.push(t1->right);
            q.push(t2->left);
        }
        return true;
    }
};
📈 Time & Space Complexity
Approach       Time Complexity   Space Complexity
Recursive DFS  O(N)              O(H)
Iterative BFS  O(N)              O(W)
N: Number of nodes in the tree.

H: Height of the tree. This is the space for the recursion call stack. For a balanced tree, H approx logN. For a skewed tree, H = N.

W: Maximum width of the tree. This is the space for the queue. For a complete binary tree, W approx N/2.

🏷️ Tags
#Tree #DepthFirstSearch #BreadthFirstSearch #Recursion #LeetCode-Easy