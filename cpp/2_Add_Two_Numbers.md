# ➕ LeetCode 2: Add Two Numbers

![LeetCode](https://img.shields.io/badge/LeetCode-2-blue?style=for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Linked%20List%2C%20Math-brightgreen?style=for-the-badge)

---

## 📘 Problem Statement

> You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
>
> You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

## 📥 Example Inputs

### ✅ Example 1:
```
**Input:**
l1 = [2,4,3], l2 = [5,6,4]
Output:
[7,0,8]
Explanation: 342 + 465 = 807.
```
---
✅ Example 2:
```
Input:
l1 = [0], l2 = [0]
Output:[0]
```
---
✅ Example 3:

```
Input:
l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output:
[8,9,9,9,0,0,0,1
```
---
## 📌 Constraints
The number of nodes in each linked list is in the range [1, 100].

0 <= Node.val <= 9.

It is guaranteed that the list represents a number that does not have leading zeros.

## 💡 Pattern & Approach
The problem requires a **direct simulation of elementary-school addition**, moving from the **least significant digit** to the most significant.  

The "reverse order" storage of digits in the linked lists makes this straightforward.

---

## 🔍 Approach: Elementary Math Simulation

We iterate through both lists simultaneously, just like adding numbers on paper column by column.  
At each step, we add digits plus any carry from the previous step.  
- The **unit digit** of the sum becomes the new node.  
- The **tens digit** (if any) becomes the carry for the next calculation.  

---

### 📝 Steps
1. **Initialize:**
   - Create a dummy head node to simplify handling the start of the result list.  
   - Initialize `carry = 0`.

2. **Iterate Through Lists:**
   - Loop while `l1`, `l2`, or `carry` is non-zero.  
   - If a list ends, treat its missing values as `0`.

3. **Calculate Sum:**
   - `sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry`.

4. **Create New Node:**
   - New node value = `sum % 10`.  
   - Append this node to the result list.

5. **Update Carry:**
   - `carry = sum / 10`.

6. **Return Result:**
   - The final answer is `dummy->next`.

---

## 🏃‍♂️ Dry Run

**Example:**  
`l1 = [2,4,3]`, `l2 = [5,6,4]`

| l1 Val | l2 Val | carry (in) | sum | New Node (`sum % 10`) | carry (out) | Result List |
|--------|--------|------------|-----|-----------------------|--------------|-------------|
| 2      | 5      | 0          | 7   | 7                     | 0            | [7]         |
| 4      | 6      | 0          | 10  | 0                     | 1            | [7, 0]      |
| 3      | 4      | 1          | 8   | 8                     | 0            | [7, 0, 8]   |

---

✅ **Conclusion:**  
Both lists are now `null` and `carry = 0`.  
The loop terminates, and the **final answer** is:  
```cpp
[7, 0, 8]
```
---
💻 C++ Code
```

/**
 * Definition for singly-linked list.
 * struct ListNode {
 * int val;
 * ListNode *next;
 * ListNode() : val(0), next(nullptr) {}
 * ListNode(int x) : val(x), next(nullptr) {}
 * ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Dummy head to simplify list creation
        ListNode* dummy = new ListNode(0);
        ListNode* l3 = dummy;
        int carry = 0;

        // Loop until both lists are processed and no carry is left
        while (l1 != nullptr || l2 != nullptr || carry) {
            int sum = carry;

            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }

            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }

            // Update carry for the next iteration
            carry = sum / 10;
            // Create a new node with the unit digit of the sum
            l3->next = new ListNode(sum % 10);
            l3 = l3->next;
        }
        
        // The result list starts after the dummy node
        return dummy->next;
    }
};
```
---

## 📈 Time & Space Complexity
Complexity	Value	Justification
Time	O(max(m,n))	We iterate through the lists once. The number of iterations is determined by the length of the longer list (m or n).
Space	O(max(m,n))	The length of the new result list is at most max(m, n) + 1. This is the dominant factor for space usage.
---
🏷️ Tags
#LinkedList #Math #Recursion #LeetCode-Medium
