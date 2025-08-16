# 🔄 LeetCode 141: Linked List Cycle

![LeetCode](https://img.shields.io/badge/LeetCode-141-blue?style=for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Two%20Pointers%2C%20Linked%20List-brightgreen?style=for-the-badge)

---

## 📘 Problem Statement

> Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
>
> There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.
>
> Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

---

## 📥 Example Inputs

### ✅ Example 1:

**Input:**
```
head = [3,2,0,-4], pos = 1
Output:
true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```
---


✅ Example 2:
```
Input:
head = [1,2], pos = 0
Output:
true
Explanation: There is a cycle where the tail connects to the 0th node.
```
---
✅ Example 3:
```
Input:
head = [1], pos = -1
Output:
false
Explanation: There is no cycle in the linked list.
```
---
📌 Constraints
The number of the nodes in the list is in the range [0, 10^4].

-10^5 <= Node.val <= 10^5

pos is -1 or a valid index in the linked-list.
---

## 💡 Pattern & Approach
There are two common ways to solve this problem:
1. **Hash Set** (Tracking Visited Nodes)
2. **Floyd’s Tortoise and Hare Algorithm** (Two Pointers – Optimal Space)

---

## **Approach 1: Hash Set (Tracking Visited Nodes)**

### 🔍 The Logic
We store each visited node in a hash set and check if we’ve seen it before.

**Steps:**
1. **Initialize a Hash Set:**  
   Create a set to store pointers (references) to visited nodes.
2. **Traverse the List:**  
   Start from `head` and move one node at a time.
3. **Check for Duplicates:**  
   - If the current node is already in the set → **Cycle detected** → return `true`.
   - Else, add it to the set and continue.
4. **No Cycle Found:**  
   If we reach `NULL`, return `false`.

---

## **Approach 2: Floyd’s Tortoise and Hare Algorithm (Two Pointers)**

### 🔍 The Logic
Uses **constant space** by having two pointers moving at different speeds.

**Steps:**
1. **Initialize Pointers:**  
   - `slow` (tortoise) → moves **1 step** at a time.  
   - `fast` (hare) → moves **2 steps** at a time.  
   Both start at `head`.
2. **Traverse:**  
   Move `slow` and `fast` according to their speeds.
3. **Check for Collision:**
   - If `fast` or `fast.next` becomes `NULL` → No cycle → return `false`.
   - If `slow == fast` → Cycle detected → return `true`.

---

## 🏃‍♂️ Dry Run (Tortoise & Hare)

**Example:**  
`head = [3, 2, 0, -4]` with a cycle where `-4` points back to `2`.

| Step | slow Node | fast Node | slow == fast? |
|------|-----------|-----------|---------------|
| 0    | 3         | 3         | Yes (Initial) |
| 1    | 2         | 0         | No            |
| 2    | 0         | 2         | No            |
| 3    | -4        | -4        | **Yes**       |

✅ **Conclusion:** Pointers meet at `-4` → Cycle detected.

---
💻 C++ Code
Approach 1: Hash Map Solution
C++
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 * int val;
 * ListNode *next;
 * ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <map>

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (!head) {
            return false;
        }
        // Use a map to keep track of visited nodes
        std::map<ListNode*, bool> visited;
        
        while (head) {
            // If the current node is already in our map, we have a cycle
            if (visited[head] == true) {
                return true;
            }
            
            // Otherwise, mark it as visited and move to the next node
            visited[head] = true;
            head = head->next;
        }
        
        // If we reach the end of the list, there is no cycle
        return false;
    }
};
```
---
Approach 2: Two Pointers (Optimal) Solution
C++
```
class Solution {
public:
    bool hasCycle(ListNode *head) {
        // Edge case: empty or single-node list has no cycle
        if (!head || !head->next) {
            return false;
        }

        ListNode *slow = head;
        ListNode *fast = head;

        // Traverse until the fast pointer reaches the end
        while (fast && fast->next) {
            slow = slow->next;          // Move slow pointer by 1
            fast = fast->next->next;    // Move fast pointer by 2

            // If pointers meet, a cycle exists
            if (slow == fast) {
                return true;
            }
        }
        
        // If the loop finishes, no cycle was found
        return false;
    }
};

```
---
📈 Time & Space Complexity
Approach	Time Complexity	Space Complexity
Hash Map	O(n)	O(n)
Two Pointers	O(n)	O(1)
The Two Pointers (Tortoise and Hare) approach is generally preferred due to its superior O(1) space complexity.
---
🏷️ Tags
#TwoPointers #LinkedList #HashTable #LeetCode-Easy
