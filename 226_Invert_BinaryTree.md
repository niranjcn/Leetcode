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

## 💡 Pattern & Approach
This problem can be solved using **Tree Traversal** techniques:  
- **Depth-First Search (DFS)** (recursive divide & conquer)  
- **Breadth-First Search (BFS)** (iterative level-order with a queue)

---

## 🔍 The Logic

### 🔹 Approach 1: Depth-First Search (DFS - Recursive)

1. **Base Case**  
   - If `root == null`, return `null` (nothing to invert).

2. **Swap Children**  
   - Swap the left and right child of the current node.

3. **Recursive Calls**  
   - Call `invertTree(root->left)`  
   - Call `invertTree(root->right)`

4. **Return Root**  
   - After recursion finishes, return the modified root.

---

### 🔹 Approach 2: Breadth-First Search (BFS - Iterative)

1. **Handle Empty Tree**  
   - If `root == null`, return `null`.

2. **Initialize**  
   - Create a queue and push the root.

3. **Level-Order Traversal**  
   - While queue is not empty:  
     - Dequeue current node.  
     - Swap its left and right children.  
     - Enqueue non-null children.

4. **Return Result**  
   - Once the queue is empty, the entire tree is inverted. Return root.

---

## 🏃‍♂️ Dry Run Example (DFS Flow)

Given:  
`root = [4,2,7,1,3,6,9]`

```plaintext
invertTree(4)
│
├── Swap children of node 4 → Left = 7, Right = 2
│
├── invertTree(7)
│   │
│   ├── Swap children of node 7 → Left = 9, Right = 6
│   │
│   ├── invertTree(9)
│   │   └── Swaps null children → returns
│   │
│   └── invertTree(6)
│       └── Swaps null children → returns
│
└── invertTree(2)
    │
    ├── Swap children of node 2 → Left = 3, Right = 1
    │
    ├── invertTree(3)
    │   └── Swaps null children → returns
    │
    └── invertTree(1)
        └── Swaps null children → returns

→ Final tree is fully inverted, return root(4)

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
