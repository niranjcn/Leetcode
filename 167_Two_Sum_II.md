# 🔢 LeetCode Problem 167: Two Sum II - Input Array Is Sorted

![LeetCode](https://img.shields.io/badge/LeetCode-Two%20Sum%20II-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Language](https://img.shields.io/badge/Language-C%2B%2B-blue)
![Time Complexity](https://img.shields.io/badge/Time%20Complexity-O(n)-brightgreen)
![Space Complexity](https://img.shields.io/badge/Space%20Complexity-O(1)-blueviolet)

---

## 📘 Problem Statement

Given a **1-indexed**, **sorted** array of integers `numbers`, find **two numbers** that add up to a given `target`.

> Return the indices of these two numbers as a 1-based array `[index1, index2]`, where `index1 < index2`.

- You may **not** use the same element twice.
- You must solve the problem with **constant extra space**.

---

## 📥 Example Inputs

### ✅ Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: 2 + 7 = 9

shell
Copy
Edit

### ✅ Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: 2 + 4 = 6

shell
Copy
Edit

### ✅ Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: -1 + 0 = -1

yaml
Copy
Edit

---

## 📌 Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i], target <= 1000`
- Array is **sorted** in non-decreasing order
- **Exactly one solution** exists

---

## 🔍 Approach — Two Pointer Technique

### 🧠 Logic:

1. Use two pointers:  
   - `i` at the start  
   - `j` at the end  
2. Calculate `sum = numbers[i] + numbers[j]`
3. If `sum == target`, return `[i+1, j+1]`
4. If `sum < target`, move `i` forward
5. If `sum > target`, move `j` backward

Since the array is sorted, this method guarantees finding the unique solution in linear time.

---

## 💻 C++ Code

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;
        vector<int> result;
        
        while (i < j) {
            int sum = numbers[i] + numbers[j];
            if (sum == target) {
                result.push_back(i + 1); // 1-indexed
                result.push_back(j + 1);
                break;
            } else if (sum < target) {
                i++;
            } else {
                j--;
            }
        }
        
        return result;
    }
};
```
---
```
📈 Time & Space Complexity
Complexity	Value
Time	O(n)
Space	O(1) — constant
```
---
🏷 Tags
#TwoPointers #Array #BinarySearch #Greedy #SortedInput #LeetCode-Medium
