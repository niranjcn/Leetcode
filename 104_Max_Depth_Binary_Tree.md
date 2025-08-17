# 🌳 LeetCode 104: Maximum Depth of Binary Tree

![LeetCode](https://img.shields.io/badge/LeetCode-104-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Tree%2C%20DFS%2C%20BFS-brightgreen?style=for-the-badge)

---

## 📘 Problem Statement

> Given the `root` of a binary tree, return its **maximum depth**.
>
> A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

---

## 📥 Example Inputs

### ✅ Example 1:

**Input:**
```cpp
root = [3,9,20,null,null,15,7]
Output:

C++

3
✅ Example 2:
Input:

C++

root = [1,null,2]
Output:

C++

2
📌 Constraints
The number of nodes in the tree is in the range [0, 10^4].

-100 <= Node.val <= 100.

## 💡 Pattern & Approach
This problem can be solved efficiently using **Tree Traversal** techniques:  
- **Depth-First Search (DFS)** (recursive divide & conquer)  
- **Breadth-First Search (BFS)** (iterative level-order with a queue)

---

## 🔍 The Logic

### 🔹 Approach 1: Depth-First Search (DFS - Recursive)

1. **Base Case**  
   - If the current node is `null`, return `0`.

2. **Recursive Calls**  
   - Compute depth of left subtree → `leftDepth = maxDepth(root->left)`  
   - Compute depth of right subtree → `rightDepth = maxDepth(root->right)`

3. **Combine Results**  
   - Depth of the current node = `1 + max(leftDepth, rightDepth)`

4. **Termination**  
   - The recursion ends when we return the depth of the root.

---

### 🔹 Approach 2: Breadth-First Search (BFS - Iterative)

1. **Handle Empty Tree**  
   - If `root == null`, return `0`.

2. **Initialize**  
   - Create a queue, push the `root`.  
   - Set `depth = 0`.

3. **Level-Order Traversal**  
   - While queue is not empty:  
     - Get `size = queue.size()` (number of nodes at current level)  
     - Increment `depth` (since we are at a new level)  
     - Process `size` nodes:  
       - Pop node from queue  
       - Push its non-null children (`left`, `right`)

4. **Return Result**  
   - Once queue is empty, return `depth`.

---

## 🏃‍♂️ Dry Run Example (DFS)

Given:  
`root = [3, 9, 20, null, null, 15, 7]`

| Call           | Left Depth | Right Depth | Depth at Node |
|----------------|------------|-------------|---------------|
| maxDepth(9)    | 0          | 0           | 1             |
| maxDepth(15)   | 0          | 0           | 1             |
| maxDepth(7)    | 0          | 0           | 1             |
| maxDepth(20)   | 1          | 1           | 2             |
| maxDepth(3)    | 1          | 2           | 3             |

**Final Answer:** `3`


💻 C++ Code
Approach 1: Recursive DFS
C++

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
    int maxDepth(TreeNode* root) {
        // Base case: an empty tree has a depth of 0
        if (root == nullptr) {
            return 0;
        }
        
        // Recursively find the depth of left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);

        // The depth is 1 (for the current node) + the deeper of the two subtrees
        return 1 + std::max(leftDepth, rightDepth);
    }
};
Approach 2: Iterative BFS
C++

#include <queue>

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        std::queue<TreeNode*> q;
        q.push(root);
        int depth = 0;

        while (!q.empty()) {
            // Number of nodes at the current level
            int levelSize = q.size();
            depth++; // Increment depth for the new level

            // Process all nodes at the current level
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();

                // Add children of the current node to the queue for the next level
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        return depth;
    }
};
📈 Time & Space Complexity
Approach	Time Complexity	Space Complexity
Recursive DFS	O(N)	O(H)
Iterative BFS	O(N)	O(W)

Export to Sheets
N: Number of nodes in the tree.

H: Height of the tree. This is the space for the recursion call stack. For a balanced tree, H
approx
logN. For a skewed tree, H=N.

W: Maximum width of the tree. This is the space for the queue. For a complete binary tree, W
approxN/2.

🏷️ Tags
#Tree #DepthFirstSearch #BreadthFirstSearch #Recursion #LeetCode-Easy
