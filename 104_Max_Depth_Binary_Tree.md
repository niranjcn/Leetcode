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

💡 Pattern & Approach
Finding the depth of a tree is a classic traversal problem. The two primary methods are Depth-First Search (DFS), which is naturally recursive, and Breadth-First Search (BFS), which is naturally iterative using a queue.

Approach 1: Depth-First Search (DFS) - Recursive
🔍 The Logic
This approach uses a "divide and conquer" strategy. The depth of any node is 1 plus the maximum depth of its children. We can apply this logic recursively down the tree.

Steps:
Base Case:

If the current node is null, it has no depth. Return 0.

Recursive Calls:

Recursively calculate the depth of the left subtree: leftDepth = maxDepth(root->left).

Recursively calculate the depth of the right subtree: rightDepth = maxDepth(root->right).

Combine Results:

The depth at the current node is 1 (for the node itself) plus the greater of the two subtree depths.

Return 1 + max(leftDepth, rightDepth).

Approach 2: Breadth-First Search (BFS) - Iterative
🔍 The Logic
This approach traverses the tree level by level. The maximum depth is simply the total number of levels in the tree. We use a queue to manage the nodes at each level.

Steps:
Handle Empty Tree:

If the root is null, return 0.

Initialize:

Create a queue and add the root node to it.

Initialize a depth counter to 0.

Level-Order Traversal:

Loop as long as the queue is not empty.

Inside the loop, get the size of the queue. This represents the number of nodes at the current level.

Increment depth (since we are starting a new level).

Process Each Level:

Loop size times:

Dequeue a node.

Enqueue its non-null left and right children.

Return Result:

Once the queue is empty, all levels have been processed. Return the final depth.

🏃‍♂️ Dry Run (Recursive DFS)
Example: root = [3, 9, 20, null, null, 15, 7]

The function calls would unfold like this:

maxDepth(3)
|
|--- 1 + max( maxDepth(9), maxDepth(20) )
| |
| |--- maxDepth(9)
| | |
| | |--- 1 + max( maxDepth(null), maxDepth(null) )
| | | |
| | | |--- maxDepth(null) returns 0
| | | |--- maxDepth(null) returns 0
| | |
| | `--- returns 1 + max(0, 0) = 1`
| |
| `--- maxDepth(20)`
| |
| |--- 1 + max( maxDepth(15), maxDepth(7) )
| | |
| | |--- maxDepth(15) returns 1
| | |--- maxDepth(7) returns 1
| | |
| | `--- returns 1 + max(1, 1) = 2`
|
`--- returns 1 + max(1, 2) = 3`
✅ Conclusion: The final result is 3.

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