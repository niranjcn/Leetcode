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

**Input:**
```cpp
l1 = [2,4,3], l2 = [5,6,4]
Output:

C++

[7,0,8]
Explanation: 342 + 465 = 807.

✅ Example 2:
Input:

C++

l1 = [0], l2 = [0]
Output:

C++

[0]
✅ Example 3:
Input:

C++

l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output:

C++

[8,9,9,9,0,0,0,1]
📌 Constraints
The number of nodes in each linked list is in the range [1, 100].

0 <= Node.val <= 9.

It is guaranteed that the list represents a number that does not have leading zeros.

💡 Pattern & Approach
The problem requires a direct simulation of elementary-school addition, moving from the least significant digit to the most significant. The "reverse order" storage of digits in the linked lists makes this straightforward.

Approach: Elementary Math Simulation
🔍 The Logic
We iterate through both lists simultaneously, just like adding numbers on paper column by column. We sum the digits at each position along with any carry from the previous position. The sum's unit digit forms the new node in our result list, and the tens digit is carried over to the next calculation.

Steps:
Initialize:

Create a dummy head node to simplify handling the start of the result list.

Initialize a carry variable to 0.

Iterate Through Lists:

Loop as long as l1 has nodes, l2 has nodes, or there is a carry value left over. This handles lists of different lengths and the final carry.

Calculate Sum:

For each position, calculate sum = (value from l1) + (value from l2) + carry.

If a list is shorter, treat its missing node's value as 0.

Create New Node:

The value for the new node is the last digit of the sum: sum % 10.

Append this new node to our result list.

Update Carry:

The new carry for the next position is the first digit of the sum: sum / 10.

Return Result:

The loop terminates when both lists are exhausted and there's no remaining carry. The dummy node's next pointer is the head of the final result list.

🏃‍♂️ Dry Run
Example: l1 = [2,4,3], l2 = [5,6,4]

l1 Val	l2 Val	carry (in)	sum	New Node (sum % 10)	carry (out)	Result List
2	5	0	7	7	0	[7]
4	6	0	10	0	1	[7, 0]
3	4	1	8	8	0	[7, 0, 8]

Export to Sheets
✅ Conclusion: Both lists are now null and carry is 0. The loop terminates. Final answer is [7,0,8].

💻 C++ Code
C++

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
📈 Time & Space Complexity
Complexity	Value	Justification
Time	O(
max(m,n))	We iterate through the lists once. The number of iterations is determined by the length of the longer list (m or n).
Space	O(
max(m,n))	The length of the new result list is at most max(m, n) + 1. This is the dominant factor for space usage.

Export to Sheets
🏷️ Tags
#LinkedList #Math #Recursion #LeetCode-Medium