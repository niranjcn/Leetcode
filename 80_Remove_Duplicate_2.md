# 🔁 LeetCode Problem: Remove Duplicates from Sorted Array II (Problem #80)

![LeetCode](https://img.shields.io/badge/LeetCode-Remove%20Duplicates%20II-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Language](https://img.shields.io/badge/Language-C%2B%2B-blue)
![Time Complexity](https://img.shields.io/badge/Time%20Complexity-O(n)-brightgreen)
![Space Complexity](https://img.shields.io/badge/Space%20Complexity-O(1)-blueviolet)

---

## 📘 Problem Statement

> Given a sorted array `nums`, remove the duplicates **in-place** such that each unique element appears **at most twice**.
>
> You must return the new length `k` such that the first `k` elements of `nums` contain the result.
>
> The order of the elements must remain the same. Don't use extra space.

---

## 📥 Example Inputs

### ✅ Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5
Updated nums = [1,1,2,2,3,_]

shell
Copy
Edit

### ✅ Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7
Updated nums = [0,0,1,1,2,3,3,,]

yaml
Copy
Edit

---

## 📌 Constraints

- `1 <= nums.length <= 30,000`
- `-10⁴ <= nums[i] <= 10⁴`
- `nums` is sorted in non-decreasing order

---

## 🧠 Algorithm Explanation — **Two Pointer with Counter**

### 👇 Intuition

We traverse the sorted array and:
- Count **repetitions** of the current element.
- If an element repeats **more than twice**, we **erase it** in-place.
- Else, continue normally.

> This ensures each element appears **at most 2 times** and the result is stored in the beginning of `nums`.

---

### 🧮 Step-by-Step

1. Initialize:
   - `i = 0` – tracks last unique group
   - `j = 1` – scans the array
   - `count = 1` – counts repetitions

2. Compare `nums[i]` with `nums[j]`:
   - If **equal**, increment `count`
     - If `count > 2`, remove `nums[j]` using `erase()` and continue
   - If **not equal**, reset `count` and move `i` to `j`

---

### 📷 Visual Representation

![Remove Duplicates II Visual](https://assets.leetcode.com/users/images/6f89b109-bdb3-4d45-ae00-0d7d1ebba1f0_1678895039.1268678.png)  
_Image Credit: LeetCode_

---

## 💡 C++ Code

```
cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0;
        int j = 1;
        int count = 1;

        while (j < nums.size()) {
            if (nums[i] == nums[j]) {
                count++;
                if (count > 2) {
                    nums.erase(nums.begin() + j); // Remove extra duplicates
                    continue; // Don't move j as the array has shifted
                }
                j++;
            } else {
                i = j;
                j++;
                count = 1;
            }
        }
        return nums.size(); // New valid length of array
    }
};
```
```
    📈 Time & Space Complexity
    Complexity	Value
    Time	O(n²) (due to erase() inside loop)
    Space	O(1) (in-place)

    ✅ Optimized solutions can achieve O(n) time by overwriting elements instead of erasing.
```

🏷 Tags
#Arrays #TwoPointers #InPlaceAlgorithm #LeetCode-Medium

🔗 Useful Resources
🔸 Official Problem on LeetCode

📘 Editorial with Optimized Solution