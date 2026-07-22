# 👯 LeetCode 100: Same Tree

![LeetCode](https://img.shields.io/badge/LeetCode-100-blue?style=for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Tree%2C%20DFS%2C%2C%20BFS-brightgreen?style=for-the-badge)

---

## 📘 Problem Statement

> Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
>
> Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

---

## 📥 Example Inputs

### ✅ Example 1:
```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```
---
✅ Example 2:
```Input: p = [1,2], q = [1,null,2]
Output: false
```
---
✅ Example 3:
C++
```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```
---
📌 Constraints
The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4.
---
## 💡 Pattern & Approach
This problem can be solved efficiently using **Tree Traversal** techniques:  
- **Depth-First Search (DFS)** (recursive divide & conquer)  
- **Breadth-First Search (BFS)** (iterative level-order with a queue)

---

## 🔍 The Logic

### 🔹 Approach 1: Depth-First Search (DFS - Recursive)

1. **Base Case 1 (Both Null)**  
   - If both `p` and `q` are `null`, return `true` (identical branch).

2. **Base Case 2 (Structure Mismatch)**  
   - If only one of `p` or `q` is `null`, return `false` (structure differs).

3. **Base Case 3 (Value Mismatch)**  
   - If `p->val != q->val`, return `false` (values differ).

4. **Recursive Step**  
   - If all checks pass, recursively check children:  
     `isSameTree(p->left, q->left) && isSameTree(p->right, q->right)`

---

### 🔹 Approach 2: Breadth-First Search (BFS - Iterative)

1. **Initialize**  
   - Create a queue for pairs of nodes: `{p, q}`.  
   - Push the root pair to start.

2. **Iterate and Compare**  
   - While the queue is not empty:  
     - Dequeue a pair of nodes.  
     - If both are `null`, continue.  
     - If only one is `null` or values differ, return `false`.  

3. **Enqueue Children**  
   - Push children pairs: `{p->left, q->left}` and `{p->right, q->right}`.

4. **Return Result**  
   - If the queue empties without returning `false`, all nodes matched. Return `true`.

---

## 🏃‍♂️ Dry Run Example (DFS Flow)

Given:  
`p = [1,2,1], q = [1,1,2]`

```plaintext
isSameTree(p_root(1), q_root(1))
│
├── Checks: Both nodes valid, values equal (1 == 1)
│
├── isSameTree(p_left(2), q_left(1))
│   │
│   └── Checks: Both nodes valid, values NOT equal (2 != 1)
│   └── returns false
│
└── The left subtree returned false
    The overall '&&' becomes false

→ Final result for isSameTree(p_root, q_root) = false
```
---
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Base case: Both are null, so they are identical.
        if (p == nullptr && q == nullptr) return true;
        
        // Base case: One is null, or values differ.
        if (p == nullptr || q == nullptr || p->val != q->val) {
            return false;
        }

        // Recursively check left and right subtrees.
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```
Approach 2: Iterative BFS

C++
```
#include <queue>
#include <utility>

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        std::queue<std::pair<TreeNode*, TreeNode*>> nodeQueue;
        nodeQueue.push({p, q});

        while (!nodeQueue.empty()) {
            auto [nodeP, nodeQ] = nodeQueue.front();
            nodeQueue.pop();

            if (!nodeP && !nodeQ) continue; // Both null, branch is fine.
            if (!nodeP || !nodeQ || nodeP->val != nodeQ->val) {
                return false; // Structure or value mismatch.
            }
            
            // Enqueue children for next level comparison.
            nodeQueue.push({nodeP->left, nodeQ->left});
            nodeQueue.push({nodeP->right, nodeQ->right});
        }
        
        return true; // Queue emptied, all nodes matched.
    }
};
```
---
📈 Time & Space Complexity
Approach       Time Complexity   Space Complexity
Recursive DFS  O(N)              O(H)
Iterative BFS  O(N)              O(W)
N: Number of nodes in the smaller tree.

H: Height of the tree. This is the space for the recursion call stack. For a balanced tree, H approx logN. For a skewed tree, H = N.

W: Maximum width of the tree. This is the space for the queue. For a complete binary tree, W approx N/2.
---
🏷️ Tags
#Tree #DepthFirstSearch #BreadthFirstSearch #Recursion #LeetCode-Easy
