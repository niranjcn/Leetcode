# 🎯 LeetCode 112: Path Sum

![LeetCode](https://img.shields.io/badge/LeetCode-112-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style-for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Tree%2C%20DFS%2C%20BFS-brightgreen?style-for-the-badge)

---

## 📘 Problem Statement

> Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.
>
> A **leaf** is a node with no children.

---

## 📥 Example Inputs

### ✅ Example 1:

```cpp
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The path 5 -> 4 -> 11 -> 2 sums to 22.

✅ Example 2:
C++

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: The available paths are 1->2 (sum=3) and 1->3 (sum=4). Neither equals 5.
✅ Example 3:
C++

Input: root = [], targetSum = 0
Output: false
Explanation: An empty tree has no root-to-leaf paths.
📌 Constraints
The number of nodes in the tree is in the range [0, 5000].

-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

💡 Pattern & Approach
This problem asks us to find if any single path from root to leaf satisfies a condition, which is a perfect use case for a Depth-First Search (DFS) traversal.

Depth-First Search (DFS) (recursive)

Depth-First Search (DFS) (iterative, with a stack)

🔍 The Logic
🔹 Approach 1: Depth-First Search (DFS - Recursive)
We traverse the tree from the root down, subtracting the node's value from the targetSum at each step. When we reach a leaf, we check if the remaining sum equals the leaf's value.

Base Case (Empty Node)

If the current node is null, it can't be part of a path. Return false.

Leaf Node Check

If the current node is a leaf (no left or right children), check if its value is equal to the remaining targetSum. This is the termination condition for a successful path.

Recursive Step

If it's not a leaf, calculate the newSum = targetSum - root->val.

Recursively call the function on the left and right children with this newSum.

If either the left path OR the right path returns true, it means a valid path was found.

🔹 Approach 2: Depth-First Search (DFS - Iterative)
We can simulate the recursive DFS using a stack. To keep track of the path sum, we'll store pairs of {node, current_sum} on the stack.

Handle Empty Tree

If root == null, return false.

Initialize

Create a stack and push the first pair: {root, targetSum - root->val}.

Iterative Traversal

While the stack is not empty:

Pop a {node, remaining_sum} pair.

If the node is a leaf and remaining_sum == 0, we found a valid path. Return true.

Push Children

If the node has a right child, push {node->right, remaining_sum - node->right->val}.

If the node has a left child, push {node->left, remaining_sum - node->left->val}.

Return Result

If the stack becomes empty, no valid path was found. Return false.

🏃‍♂️ Dry Run Example (DFS)
Given:
root = [5,4,8,...], targetSum = 22

hasPathSum(node(5), 22)
│
├── path_found = hasPathSum(node(4), 17) || hasPathSum(node(8), 17)
│
├── hasPathSum(node(4), 17)
│   │
│   └── path_found = hasPathSum(node(11), 13) || hasPathSum(null, 13)
│       │
│       ├── hasPathSum(node(11), 13)
│       │   │
│       │   └── path_found = hasPathSum(node(7), 2) || hasPathSum(node(2), 2)
│       │       │
│       │       ├── hasPathSum(node(7), 2) -> leaf, 7!=2, returns false
│       │       │
│       │       └── hasPathSum(node(2), 2) -> leaf, 2==2, returns true
│       │
│       └── The second part of '||' is true, so this call returns true
│
└── The first part of '||' is true, so the top-level call returns true.

→ Final result is true.
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
    bool hasPathSum(TreeNode* root, int targetSum) {
        // Base case: an empty tree has no paths.
        if (!root) {
            return false;
        }

        // Check if it's a leaf node and if the sum matches.
        if (!root->left && !root->right) {
            return targetSum == root->val;
        }

        // Subtract current node's value from the target.
        int newSum = targetSum - root->val;

        // Recursively check the left OR right subtree for a valid path.
        return hasPathSum(root->left, newSum) || hasPathSum(root->right, newSum);
    }
};
Approach 2: Iterative DFS

C++

#include <stack>
#include <utility>

class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (!root) {
            return false;
        }

        std::stack<std::pair<TreeNode*, int>> s;
        s.push({root, targetSum - root->val});

        while (!s.empty()) {
            auto [node, currentSum] = s.top();
            s.pop();

            // Check if it's a leaf node and sum is zero
            if (!node->left && !node->right && currentSum == 0) {
                return true;
            }

            // Push children with updated sum
            if (node->right) {
                s.push({node->right, currentSum - node->right->val});
            }
            if (node->left) {
                s.push({node->left, currentSum - node->left->val});
            }
        }
        
        return false;
    }
};
📈 Time & Space Complexity
Approach           Time Complexity   Space Complexity
Recursive DFS      O(N)              O(H)
Iterative DFS      O(N)              O(H)
N: Number of nodes in the tree.

H: Height of the tree. This is the space for the recursion call stack or the explicit stack. For a balanced tree, H approx logN. For a skewed tree, H = N.

🏷️ Tags
#Tree #DepthFirstSearch #BreadthFirstSearch #Recursion #LeetCode-Easy