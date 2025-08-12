# 🔡 LeetCode 3: Longest Substring Without Repeating Characters

![LeetCode](https://img.shields.io/badge/LeetCode-3-blue?style=for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Sliding%20Window%2C%20Hash%20Table-brightgreen?style=for-the-badge)

---

## 📘 Problem Statement

> Given a string `s`, find the length of the **longest substring** without duplicate characters.

---

## 📥 Example Inputs

### ✅ Example 1:

**Input:**
```
s = "abcabcbb"
Output:3
Explanation: The answer is "abc", with the length of 3.
```

----

✅ Example 2:
Input:
```
s = "bbbbb"
Output:1
Explanation: The answer is "b", with the length of 1.
```
---

✅ Example 3:
Input:
```
s = "pwwkew"
Output:3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```
---
📌 Constraints
0 <= s.length <= 5 * 10^4

s consists of English letters, digits, symbols and spaces.

---

💡 Pattern & Approach
This is a perfect problem for the Sliding Window technique combined with a Hash Set. The window represents the current substring we are examining, and the hash set provides a fast way to check if a character already exists in that window.

🔍 The Logic
We use two pointers, left and right, to define our window. We try to expand the window by moving right. If we find a duplicate character, we shrink the window from the left until the duplicate is removed.

Initialize:

left and right pointers, both at 0.

maxLen = 0 to store our final answer.

A hash set, window, to keep track of characters currently in our substring.

Iterate and Expand: We loop as long as our right pointer is within the string's bounds.

Case 1: No Duplicate Found

If the character s[right] is not in our window set:

We add s[right] to the set.

We've successfully expanded our unique substring. Update maxLen = max(maxLen, window.size()).

Increment right to continue expanding.

Case 2: Duplicate Found

If the character s[right] is already in our window set:

We have a duplicate. We must shrink the window from the left to remove the first occurrence of this character.

Remove s[left] from the set.

Increment left.

We repeat this shrink step until the duplicate is gone, at which point the loop will proceed to expand again.

Result: The loop finishes when right reaches the end of the string. The value in maxLen is our answer.

🏃‍♂️ Dry Run Example
Let's trace the algorithm with s = "abcabcbb".
Initial State: left = 0, right = 0, window = {}, maxLen = 0

right	s[right]	in window?	Action	left	window	maxLen
0	a	No	Insert a, right++, update maxLen	0	{a}	1
1	b	No	Insert b, right++, update maxLen	0	{a,b}	2
2	c	No	Insert c, right++, update maxLen	0	{a,b,c}	3
3	a	Yes	Remove s[left] (a), left++	1	{b,c}	3
3	a	No	Insert a, right++, update maxLen	1	{b,c,a}	3
4	b	Yes	Remove s[left] (b), left++	2	{c,a}	3
4	b	No	Insert b, right++, update maxLen	2	{c,a,b}	3
5	c	Yes	Remove s[left] (c), left++	3	{a,b}	3
5	c	No	Insert c, right++, update maxLen	3	{a,b,c}	3
6	b	Yes	Remove s[left] (a), left++	4	{b,c}	3
6	b	Yes	Remove s[left] (b), left++	5	{c}	3
6	b	No	Insert b, right++, update maxLen	5	{c,b}	3

Export to Sheets
The loop terminates when right reaches the end. The final answer is 3.

💻 C++ Code
```

#include <string>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        int left = 0;
        int right = 0;
        int n = s.length();
        int maxLen = 0;
        std::unordered_set<char> window;

        while (right < n) {
            // Case 1: Character is not in the window. Expand.
            if (window.find(s[right]) == window.end()) {
                window.insert(s[right]);
                maxLen = std::max(maxLen, right - left + 1);
                right++;
            } 
            // Case 2: Character is a duplicate. Shrink.
            else {
                window.erase(s[left]);
                left++;
            }
        }
        return maxLen;
    }
};

```
---
📈 Time & Space Complexity
Complexity	Value	Justification
Time	O(n)	Each character in the string s is visited at most twice—once by the right pointer and once by the left pointer. This makes the overall time complexity linear.
Space	O(k)	The space complexity is determined by the size of the hash set (window). In the worst case, the string contains all unique characters, so the space is proportional to the number of unique characters, k. k is at most min(n, m), where n is the string length and m is the size of the character set.

---
🏷️ Tags
#SlidingWindow #HashTable #String #TwoPointers #LeetCode-Medium
