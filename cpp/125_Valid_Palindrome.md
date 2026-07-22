# 🔎 LeetCode Problem: Valid Palindrome (Problem #125)

![LeetCode](https://img.shields.io/badge/LeetCode-Valid%20Palindrome-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-success)
![Language](https://img.shields.io/badge/Language-C%2B%2B-blue)
![Time Complexity](https://img.shields.io/badge/Time%20Complexity-O(n)-brightgreen)
![Space Complexity](https://img.shields.io/badge/Space%20Complexity-O(n)-blueviolet)

---

## 📘 Problem Statement

> A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
>
> Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

---

## 📥 Example Inputs

### ✅ Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: After cleaning, "amanaplanacanalpanama" is a palindrome.

shell
Copy
Edit

### ✅ Example 2:
Input: s = "race a car"
Output: false
Explanation: After cleaning, "raceacar" is not a palindrome.

shell
Copy
Edit

### ✅ Example 3:
Input: s = " "
Output: true
Explanation: After removing non-alphanumeric characters, the string is empty, which is a palindrome.

yaml
Copy
Edit

---

## 📌 Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

---

## 🧠 Algorithm Explanation — **Clean and Compare**

### 👇 Steps:

1. Traverse the input string and build a new string `str` by:
   - Converting uppercase to lowercase.
   - Ignoring non-alphanumeric characters.

2. Create a reversed copy of `str`.

3. Compare the cleaned string with its reversed version:
   - If equal, return `true`.
   - Otherwise, return `false`.

---

### 📷 Visual Explanation

![Palindrome Check Illustration](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Palindrome_diagram.svg/320px-Palindrome_diagram.svg.png)  
_Image Credit: Wikimedia Commons_

---

## 💡 C++ Code

cpp
```
class Solution {
public:
    bool isPalindrome(string s) {
        string str;
        for (char ch : s) {
            ch = tolower(ch);
            if (isalnum(ch)) {
                str += ch;
            }
        }
        string rev = str;
        reverse(rev.begin(), rev.end());
        return str == rev;
    }
};
```


```
📈 Time & Space Complexity
Complexity	Value
Time	O(n)
Space	O(n)
```

🏷 Tags
#Strings #TwoPointers #Palindrome #LeetCode-Easy


🔗 Useful Links
🔸 Official Problem on LeetCode

