# 🚀 LeetCode Problem: Merge Sorted Array (Problem #88)

![LeetCode](https://img.shields.io/badge/LeetCode-Merge%20Sorted%20Array-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-success)
![Language](https://img.shields.io/badge/Language-C%2B%2B-blue)
![Time Complexity](https://img.shields.io/badge/Time%20Complexity-O(m%20%2B%20n)-brightgreen)
![Space Complexity](https://img.shields.io/badge/Space%20Complexity-O(1)-blueviolet)

---

## 🧠 Problem Statement

> You are given two sorted integer arrays `nums1` and `nums2`, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.
>
> Merge `nums2` into `nums1` as one sorted array in non-decreasing order. The final sorted array should be **stored in** `nums1`, not returned.

---

## 📥 Example Inputs

### ✅ Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

shell
Copy
Edit

### ✅ Example 2:
Input: nums1 = [1], m = 1
nums2 = [], n = 0
Output: [1]

shell
Copy
Edit

### ✅ Example 3:
Input: nums1 = [0], m = 0
nums2 = [1], n = 1
Output: [1]

markdown
Copy
Edit

---

## 📌 Constraints

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `-10⁹ <= nums1[i], nums2[j] <= 10⁹`

---

## 🧩 Algorithm Used — **Two Pointer Approach (from end)**

### 👇 Logic Explanation:

We take three pointers:
- `i` → Points to the last element in `nums1` (excluding extra 0s).
- `j` → Points to the last element in `nums2`.
- `k` → Points to the last position in `nums1` (where the merged array will end up).

We start comparing elements from the end:
- If `nums1[i] > nums2[j]`, place `nums1[i]` at position `k`.
- Otherwise, place `nums2[j]` at position `k`.
- Move the respective pointers backward.

This way, we **avoid overwriting** elements in `nums1`.

### 📷 Visual Representation:

![Merge Process](https://miro.medium.com/v2/resize:fit:828/format:webp/1*9wK5Vf-jSFTcZ_WTjGrUiw.png)

_Image Credit: [Medium](https://medium.com/@namanbhalla/merge-sorted-array-leetcode-88-c19ef6f7f778)_

---

## 💡 C++ Code

```cpp
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1;        // Pointer for nums1 (excluding trailing 0s)
        int j = n - 1;        // Pointer for nums2
        int k = m + n - 1;    // Pointer for merged position in nums1

        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }
    }
};
🏁 Output
Once this function runs, nums1 will contain the merged and sorted array in-place.

📈 Time & Space Complexity
Complexity	Value
Time	O(m + n)
Space	O(1) (in-place)

🧪 Test It Online
Try this solution live on:
🔗 LeetCode Playground

📚 Tags
#Arrays #TwoPointers #InPlaceAlgorithm #Sorting #LeetCode-Easy