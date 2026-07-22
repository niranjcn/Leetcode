Markdown

# 🌳 LeetCode 222: Count Complete Tree Nodes

![LeetCode](https://img.shields.io/badge/LeetCode-222-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style-for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Tree%2C%20Binary%20Search-brightgreen?style-for-the-badge)

---

## 📘 Problem Statement

> Given the `root` of a **complete** binary tree, return the number of the nodes in the tree.
>
> According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible.
>
> **Design an algorithm that runs in less than `O(n)` time complexity.**

---

## 📥 Example Inputs

### ✅ Example 1:

```cpp
Input: root = [1,2,3,4,5,6]
Output: 6
✅ Example 2:
C++

Input: root = []
Output: 0
✅ Example 3:
C++

Input: root = [1]
Output: 1
📌 Constraints
The number of nodes in the tree is in the range [0, 5 * 10^4].

0 <= Node.val <= 5 * 10^4.

The tree is guaranteed to be complete.

💡 Pattern & Approach
The challenge is to find a solution faster than the standard O(n) traversal. This requires leveraging the special properties of a complete binary tree.

Simple Traversal (DFS) (Correct but too slow, O(n))

Optimized Traversal using Height (Uses binary search properties, O(log n * log n))

🔍 The Logic
🔹 Approach 1: Simple Traversal (DFS - Recursive)
This is the standard way to count nodes in any binary tree. It visits every node. While it gives the correct answer, it does not meet the problem's time complexity constraint.

Base Case

If the current node is null, it contributes 0 nodes. Return 0.

Recursive Step

The total count is 1 (for the current node) + the count from the left subtree + the count from the right subtree.

🔹 Approach 2: Optimized DFS using Tree Height
This approach exploits the complete tree property. For any subtree, if it's a perfect binary tree, we can calculate its node count in O(1) using a formula instead of traversing it.

Calculate Leftmost and Rightmost Heights

For any given root, calculate its height by only following left pointers (leftHeight).

Separately, calculate its height by only following right pointers (rightHeight).

Check for a Perfect Subtree

If leftHeight == rightHeight, it means the subtree rooted at root is a perfect binary tree. All levels are completely full.

Use the Formula

The number of nodes in a perfect binary tree of height h is 2^h - 1. We can calculate this quickly as (1 << h) - 1. If we find a perfect subtree, we use this formula and stop recursing down that path.

Recurse if Not Perfect

If leftHeight != rightHeight, the subtree is complete but not perfect. We don't have a shortcut, so we fall back to the standard recursion for this node: 1 + countNodes(root->left) + countNodes(root->right).

The optimization comes from pruning large, perfect subtrees from the traversal.

🏃‍♂️ Dry Run Example (Optimized DFS)
Given:
root = [1,2,3,4,5,6]

countNodes(1)
│
├── Get left height of node 1 (1->2->4) -> lh = 3
├── Get right height of node 1 (1->3->6) -> rh = 3
│   └── Whoops, a simple right-path check isn't enough. We must check if the subtree is perfect.
│
├── Let's re-run with the correct check:
│
├── countNodes(1):
│   ├── Leftmost height from (1) is 3 (1->2->4). Rightmost height is 3 (1->3->6). NOT PERFECT.
│   └── Must recurse: return 1 + countNodes(2) + countNodes(3)
│
├── countNodes(2):
│   ├── Leftmost height from (2) is 2 (2->4). Rightmost height is 2 (2->5). PERFECT.
│   └── It's a perfect subtree of height 2. Count = 2^2 - 1 = 3. Returns 3.
│
├── countNodes(3):
│   ├── Leftmost height from (3) is 2 (3->6). Rightmost height is 1 (3 itself). NOT PERFECT.
│   └── Must recurse: return 1 + countNodes(6) + countNodes(null)
│       │
│       ├── countNodes(6) -> Perfect subtree of height 1. Count = 2^1 - 1 = 1. Returns 1.
│       └── countNodes(null) -> Returns 0.
│   └── returns 1 + 1 + 0 = 2.
│
└── Final calculation: 1 + 3 (from left) + 2 (from right) = 6.

→ Final result is 6.
💻 C++ Code
Approach 1: Simple Traversal (O(n))

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
    int countNodes(TreeNode* root) {
        if (!root) {
            return 0;
        }
        // This is correct but does not meet the sub-O(n) requirement.
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};
Approach 2: Optimized DFS (O(log n * log n))

C++

class Solution {
public:
    int countNodes(TreeNode* root) {
        if (!root) {
            return 0;
        }

        int leftHeight = 0;
        TreeNode* l = root;
        while (l) {
            leftHeight++;
            l = l->left;
        }

        int rightHeight = 0;
        TreeNode* r = root;
        while (r) {
            rightHeight++;
            r = r->right;
        }

        // If heights are equal, it's a perfect binary tree
        if (leftHeight == rightHeight) {
            return (1 << leftHeight) - 1; // Equivalent to pow(2, h) - 1
        }

        // Otherwise, recurse on children
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};
📈 Time & Space Complexity
Approach           Time Complexity        Space Complexity
Simple Traversal   O(N)                   O(H)
Optimized DFS      O((log N)^2)           O(H)
N: Number of nodes in the tree.

H: Height of the tree (which is log N for a complete tree).

Why O((log N)^2)? The path of recursive calls will go down only one side of the tree, taking O(H) or O(log N) steps. At each step, we calculate the height, which also takes O(H) or O(log N) time. This results in O(log N * log N).

🏷️ Tags
#Tree #BinarySearch #DepthFirstSearch #LeetCode-Easy