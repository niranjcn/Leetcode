# ↔️ LeetCode 226: Invert Binary Tree

![LeetCode](https://img.shields.io/badge/LeetCode-226-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style-for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Tree%2C%20DFS%2C%20BFS-brightgreen?style-for-the-badge)

---

## 📘 Problem Statement

> Given the `root` of a binary tree, invert the tree, and return its root.

---

## 📥 Example Inputs

### ✅ Example 1:

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```
---
✅ Example 2:
C++
```
Input: root = [2,1,3]
Output: [2,3,1]
```
---
✅ Example 3:
C++
```
Input: root = []
Output: []
```
---
📌 Constraints
The number of nodes in the tree is in the range [0, 100].

-100 <= Node.val <= 100.

💡 Pattern & Approach
This is a classic tree traversal problem where the structure of the tree is modified. The inversion can be performed using either a top-down or bottom-up approach.

Depth-First Search (DFS) (recursive)

Breadth-First Search (BFS) (iterative)

---

🔍 The Logic
🔹 Approach 1: Depth-First Search (DFS - Recursive)
This approach recursively traverses the tree. At each node, it swaps the left and right children.

Base Case

If the current node is null, there is nothing to invert, so return null.

Swap Children

Swap the current node's left and right child pointers.

Recursive Calls

Recursively call the function on the (new) left child: invertTree(root->left).

Recursively call the function on the (new) right child: invertTree(root->right).

Return Root

After all recursive calls are complete, the entire tree is inverted. Return the root.

🔹 Approach 2: Breadth-First Search (BFS - Iterative)
This approach inverts the tree level by level using a queue.

Handle Empty Tree

If root == null, return null.

Initialize

Create a queue and push the root onto it.

Level-Order Traversal

While the queue is not empty:

Dequeue the current node.

Swap its left and right children.

If the (new) left child is not null, enqueue it.

If the (new) right child is not null, enqueue it.

Return Result

Once the queue is empty, all nodes have been processed. Return the root.

🏃‍♂️ Dry Run Example (DFS)
Given:
root = [4,2,7,1,3,6,9]

invertTree(4)
│
├── Swap children of node 4. Left becomes 7, Right becomes 2.
│
├── invertTree(node 7)
│   │
│   ├── Swap children of node 7. Left becomes 9, Right becomes 6.
│   │
│   ├── invertTree(node 9) → Swaps its null children. Returns.
│   └── invertTree(node 6) → Swaps its null children. Returns.
│
└── invertTree(node 2)
    │
    ├── Swap children of node 2. Left becomes 3, Right becomes 1.
    │
    ├── invertTree(node 3) → Swaps its null children. Returns.
    └── invertTree(node 1) → Swaps its null children. Returns.

→ Final tree root is returned.
💻 C++ Code
Approach 1: Recursive DFS

C++
```
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
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the node is null, do nothing.
        if (root == nullptr) {
            return nullptr;
        }
        
        // Swap the left and right children.
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // Recursively invert the left and right subtrees.
        invertTree(root->left);
        invertTree(root->right);
        
        return root;
    }

};
```
---
Approach 2: Iterative BFS

C++
```
#include <queue>

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }

        std::queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* current = q.front();
            q.pop();

            // Swap the children
            TreeNode* temp = current->left;
            current->left = current->right;
            current->right = temp;

            // Enqueue children if they exist
            if (current->left) {
                q.push(current->left);
            }
            if (current->right) {
                q.push(current->right);
            }
        }
        
        return root;
    }
};
```
---
📈 Time & Space Complexity
Approach       Time Complexity   Space Complexity
Recursive DFS  O(N)              O(H)
Iterative BFS  O(N)              O(W)
N: Number of nodes in the tree.

H: Height of the tree. This is the space for the recursion call stack. For a balanced tree, H approx logN. For a skewed tree, H = N.

W: Maximum width of the tree. This is the space for the queue. For a complete binary tree, W approx N/2.
---
🏷️ Tags
#Tree #DepthFirstSearch #BreadthFirstSearch #Recursion #LeetCode-Easy
