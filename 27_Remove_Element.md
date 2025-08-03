# 🧹 LeetCode Problem: Remove Element (Problem #27)

![LeetCode](https://img.shields.io/badge/LeetCode-Remove%20Element-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-success)
![Language](https://img.shields.io/badge/Language-C%2B%2B-blue)
![Time Complexity](https://img.shields.io/badge/Time%20Complexity-O(n)-brightgreen)
![Space Complexity](https://img.shields.io/badge/Space%20Complexity-O(1)-blueviolet)

---

## 📘 Problem Statement

> Given an array `nums` and an integer `val`, remove all instances of `val` **in-place** and return the new length of the array.
>
> The order of elements can be changed, and values beyond the returned length do not matter.

---

## 📥 Example Inputs

### ✅ Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2
Updated nums = [2,2,,]



### ✅ Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5
Updated nums = [0,1,4,0,3,,,_]



---

## 📌 Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

---

## 🧠 Algorithm Explanation — **Two Pointer Swap Approach**

### 🎯 Goal:

1. Remove all instances of `val`.
2. Keep the remaining elements in the front `k` positions of the array.
3. Return `k`.

---

### 👇 Logic Breakdown:

We use **two pointers**:
- `i` → for scanning the array
- `j` → for tracking the next valid position for a non-`val` element

Steps:
- If `nums[i] != val` and `nums[j] == val`, we **swap** them.
- If `nums[j] != val`, just **move forward**.
- In the end, `j` will represent the number of non-`val` elements in the array.

---

### 📷 Visual Representation

![Remove Element Visual](https://assets.leetcode.com/users/images/00eac302-e022-4df7-8992-3e177e7b6f2a_1678668757.9795737.png)  
_Image Source: LeetCode_

---

## 💡 C++ Code

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        int j = 0;

        for(i = 0; i < nums.size(); i++) {
            if(nums[i] == val) {
                continue;
            } else if(nums[j] == val) {
                swap(nums[i], nums[j]);
                j++;
            } else {
                j++;
            }
        }

        return j;
    }
};
📈 Time & Space Complexity
Complexity	Value
Time	O(n)
Space	O(1) (In-place)

🧪 How It’s Tested
LeetCode uses a custom judge:

cpp
Copy
Edit
int[] nums = [...];
int val = ...;
int k = removeElement(nums, val);
sort(nums, 0, k);
for (int i = 0; i < k; i++) {
    assert(nums[i] == expectedNums[i]);
}
🧷 Tags
#Arrays #TwoPointers #InPlaceAlgorithm #LeetCode-Easy

🔗 Useful Links
🔸 Official Problem Link

🔸 Related Visual Guide
