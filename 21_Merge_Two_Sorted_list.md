# 🔗 LeetCode 21: Merge Two Sorted Lists

![LeetCode](https://img.shields.io/badge/LeetCode-21-blue?style=for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Linked%20List%2C%20Recursion-brightgreen?style=for-the-badge)

---

## 📘 Problem Statement

> You are given the heads of two sorted linked lists `list1` and `list2`.
>
> Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.
>
> Return the head of the merged linked list.

---

## 📥 Example Inputs

### ✅ Example 1:
```
Input:
list1 = [1,2,4], list2 = [1,3,4]
Output:
[1,1,2,3,4,4]
```
---
✅ Example 2:
```Input:
list1 = [], list2 = []
Output:
[]
```
---
✅ Example 3:
```Input:
list1 = [], list2 = [0]
Output:
[0]
```
---
📌 Constraints
The number of nodes in both lists is in the range [0, 50].

-100 <= Node.val <= 100.

Both list1 and list2 are sorted in non-decreasing order.

---

## 💡 Pattern & Approach
The core pattern is an **iterative two-pointer merge**, similar to the merge step in **Merge Sort**.  

We can solve this using two strategies:  
1. **Creating a new list** (extra memory)  
2. **Splicing nodes in-place** (more efficient)

---

## 🔹 Approach 1: Iterative Merge by Creating New Nodes

### 🔍 The Logic
We build a completely **new list** by iterating through both input lists and creating a new node for each selected element.  

### 📝 Steps
1. **Initialize:**
   - Create a dummy head node.  
   - Maintain a `tail` pointer starting at the dummy.

2. **Iterate & Compare:**
   - While both `list1` and `list2` are non-null:  
     - Compare values.  
     - Pick the smaller one.  

3. **Create & Append:**
   - Create a new node with the smaller value.  
   - Attach it to `tail->next`.  
   - Move `tail` forward.  

4. **Advance Pointers:**
   - Move the pointer (`list1` or `list2`) from which the smaller value was chosen.  

5. **Append Remainder:**
   - Attach the remaining list (if any) to `tail`.  

6. **Return Result:**
   - Final merged list starts at `dummy->next`.  

---

## 🔹 Approach 2: Iterative Merge by Splicing Nodes (In-Place)

### 🔍 The Logic
Instead of creating new nodes, we **rearrange existing nodes’ pointers** to form the merged list.  
This is more **space-efficient** (no extra allocations).

### 📝 Steps
1. **Handle Edge Cases:**
   - If one list is empty → return the other list.  

2. **Initialize Pointers:**
   - Set the head of the merged list by comparing the first nodes of `list1` and `list2`.  
   - Use a `tail` pointer starting at this head.  

3. **Iterate & Splice:**
   - While both lists are non-null:  
     - Compare `list1->val` and `list2->val`.  
     - Attach the smaller node to `tail->next`.  
     - Advance both `tail` and the chosen list pointer.  

4. **Append Remainder:**
   - If one list ends, append the remaining list.  

5. **Return Result:**
   - Return the merged head.  

---

## 🏃‍♂️ Dry Run (In-Place Splicing)

**Example:**  
`list1 = [1,2,4]`, `list2 = [1,3,4]`

| l1 | l2 | l1.val <= l2.val? | Action | Merged List State |
|----|----|-------------------|--------|-------------------|
| 1  | 1  | Yes | Head = l1. Tail = l1. Advance l1. | 1 |
| 2  | 1  | No  | tail->next = l2. Tail = l2. Advance l2. | 1 → 1 |
| 2  | 3  | Yes | tail->next = l1. Tail = l1. Advance l1. | 1 → 1 → 2 |
| 4  | 3  | No  | tail->next = l2. Tail = l2. Advance l2. | 1 → 1 → 2 → 3 |
| 4  | 4  | Yes | tail->next = l1. Tail = l1. Advance l1. | 1 → 1 → 2 → 3 → 4 |
| null | 4 | (l1 is null) | Append remaining l2. | 1 → 1 → 2 → 3 → 4 → 4 |

---

✅ **Conclusion:**  
The loop finishes when one list is null.  
Remaining nodes (if any) are appended.  
The final merged list is:  
```
[1, 1, 2, 3, 4, 4]
```

---
💻 C++ Code
Approach 1: Creating New Nodes
C++
```
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                // Create a new node and append
                tail->next = new ListNode(list1->val);
                list1 = list1->next;
            } else {
                tail->next = new ListNode(list2->val);
                list2 = list2->next;
            }
            tail = tail->next;
        }

        // Append the remaining nodes by creating new nodes
        while (list1 != nullptr) {
            tail->next = new ListNode(list1->val);
            list1 = list1->next;
            tail = tail->next;
        }
        while (list2 != nullptr) {
            tail->next = new ListNode(list2->val);
            list2 = list2->next;
            tail = tail->next;
        }

        return dummy->next;
    }
};
```
---

Approach 2: Splicing Nodes (In-Place, 0ms)
C++
```
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Handle edge cases where one list is empty
        if (!list1) return list2;
        if (!list2) return list1;

        ListNode* head;
        // Determine the head of the merged list
        if (list1->val <= list2->val) {
            head = list1;
            list1 = list1->next;
        } else {
            head = list2;
            list2 = list2->next;
        }
        
        ListNode* tail = head; // tail pointer to build the list

        // Loop while both lists have nodes
        while (list1 && list2) {
            if (list1->val <= list2->val) {
                tail->next = list1; // Splice
                list1 = list1->next;
            } else {
                tail->next = list2; // Splice
                list2 = list2->next;
            }
            tail = tail->next;
        }

        // Append the remaining list
        if (list1) {
            tail->next = list1;
        } else {
            tail->next = list2;
        }
        
        return head;
    }
};
```

📈 Time & Space Complexity
Approach	Time Complexity	Space Complexity
Creating New Nodes	O(m+n)	O(m+n)
Splicing (In-Place)	O(m+n)	O(1)
The in-place splicing approach is superior as it avoids the overhead of creating new objects for every node, resulting in constant space complexity and better performance.

🏷️ Tags
#LinkedList #Recursion #TwoPointers #LeetCode-Easy
