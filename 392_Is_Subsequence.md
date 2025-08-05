# 🔗 LeetCode Problem: Is Subsequence (Problem #392)

![LeetCode](https://img.shields.io/badge/LeetCode-Is%20Subsequence-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-success)
![Language](https://img.shields.io/badge/Language-C%2B%2B-blue)
![Time Complexity](https://img.shields.io/badge/Time%20Complexity-O(n)-brightgreen)
![Space Complexity](https://img.shields.io/badge/Space%20Complexity-O(1)-blueviolet)

---

## 📘 Problem Statement

> Given two strings `s` and `t`, return `true` if `s` is a **subsequence** of `t`, or `false` otherwise.

A **subsequence** is formed by deleting **zero or more characters** from the original string **without changing the order** of the remaining characters.

---

## 📥 Example Inputs

### ✅ Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Explanation: "abc" appears in order within "ahbgdc".

shell
Copy
Edit

### ✅ Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
Explanation: Characters from s do not maintain order in t.

yaml
Copy
Edit

---

## 📌 Constraints

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.

---

## 🧠 Algorithm Explanation — **Two Pointer Technique**

### 🔍 Intuition:

We use two pointers:
- `i` → for `s` (target subsequence)
- `j` → for `t` (main string)

Loop through `t`, and every time a character matches `s[i]`, move `i` forward.  
At the end, if `i == s.length()`, all characters from `s` were matched in order — hence it's a subsequence.

---

### 📷 Visual Illustration

| s (subsequence) | a | b | c |  |  |   |
|------------------|---|---|---|---|---|---|
| t (main string)  | a | h | b | g | d | c |
| Pointers         | ↑ |   |   |   |   |   |

At each matching step, `i` moves forward — if all characters in `s` are found in sequence in `t`, return `true`.

---

## 💡 C++ Code

cpp
```
#include <string>
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;

        while (i < s.length() && j < t.length()) {
            if (s[i] == t[j]) {
                i++;
            }
            j++;
        }

        return i == s.length(); // All characters in 's' matched in order
    }
};
```
```
📈 Time & Space Complexity
Complexity	Value
Time	O(n) where n = length of t
Space	O(1) — constant space
```

🏷 Tags
#Strings #TwoPointers #Greedy #LeetCode-Easy
