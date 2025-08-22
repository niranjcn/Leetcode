# 🔡 LeetCode 242: Valid Anagram

![LeetCode](https://img.shields.io/badge/LeetCode-242-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style-for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Hash%20Table%2C%20String%2C%20Sorting-brightgreen?style-for-the-badge)

---

## 📘 Problem Statement

> Given two strings `s` and `t`, return `true` if `t` is an **anagram** of `s`, and `false` otherwise.
>
> An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

## 📥 Example Inputs

### ✅ Example 1:
```cpp
Input: s = "anagram", t = "nagaram"
Output: true
✅ Example 2:
C++

Input: s = "rat", t = "car"
Output: false
📌 Constraints
1 <= s.length, t.length <= 5 * 10^4

s and t consist of lowercase English letters.

💡 Pattern & Approach
The definition of an anagram is that two words must have the exact same characters with the exact same frequencies. This leads to two primary solutions:

Frequency Counting (using a Hash Table or Array)

Sorting (and comparing the resulting strings)

🔍 The Logic
🔹 Approach 1: Frequency Counting (Hash Table / Array)
We can count the occurrences of each character in one string and then "check off" those characters using the second string.

Length Check

If the strings have different lengths, they cannot be anagrams. Return false immediately.

Initialize Counter

Create an array count of size 26 (for 'a' through 'z'), initialized to all zeros.

Count Characters in s

Iterate through string s and increment the count for each character. count[char - 'a']++.

Decrement for t

Iterate through string t. For each character, decrement its count in the array.

Check for Mismatch

If at any point a character's count drops below zero, it means t has more of that character than s. They are not anagrams, so return false.

Return Result

If the second loop completes, it means the character frequencies were identical. Return true.

🔹 Approach 2: Sorting
If two strings are anagrams, they are made of the same letters. Therefore, sorting them alphabetically will result in identical strings.

Length Check

If the string lengths are different, return false.

Sort s

Sort the characters of string s in place.

Sort t

Sort the characters of string t in place.

Compare

Return the result of comparing the two sorted strings. If they are equal, they are anagrams.

🏃‍♂️ Dry Run Example (Frequency Counting)
Given:
s = "anagram", t = "nagaram"

Action	String	Character	count state (relevant chars)	Note
Initialize	-	-	{'a':0, 'n':0, 'g':0, 'r':0, 'm':0}	Lengths are equal (7).
Scan s	s	'a'	{'a':1}	
s	'n'	{'a':1, 'n':1}	
s	'a'	{'a':2, 'n':1}	
s	'g'	{'a':2, 'n':1, 'g':1}	
s	'r'	{'a':2, 'n':1, 'g':1, 'r':1}	
s	'a'	{'a':3, 'n':1, 'g':1, 'r':1}	
s	'm'	{'a':3, 'n':1, 'g':1, 'r':1, 'm':1}	Scan of s is complete.
Scan t	t	'n'	{'a':3, 'n':0, 'g':1, 'r':1, 'm':1}	Decrement count['n'].
t	'a'	{'a':2, 'n':0, 'g':1, 'r':1, 'm':1}	Decrement count['a'].
t	'g'	{'a':2, 'n':0, 'g':0, 'r':1, 'm':1}	Decrement count['g'].
t	'a'	{'a':1, 'n':0, 'g':0, 'r':1, 'm':1}	Decrement count['a'].
t	'r'	{'a':1, 'n':0, 'g':0, 'r':0, 'm':1}	Decrement count['r'].
t	'a'	{'a':0, 'n':0, 'g':0, 'r':0, 'm':1}	Decrement count['a'].
t	'm'	{'a':0, 'n':0, 'g':0, 'r':0, 'm':0}	Decrement count['m'].

Export to Sheets
✅ Conclusion: The loop for t completed without any count going below zero. Return true.

💻 C++ Code
Approach 1: Frequency Counting

C++

#include <string>
#include <unordered_map>
#include <vector> // For array optimization

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        // Use a vector as a frequency map for lowercase letters
        std::vector<int> counts(26, 0);
        
        // Increment counts for string s
        for (char c : s) {
            counts[c - 'a']++;
        }
        
        // Decrement counts for string t
        for (char c : t) {
            counts[c - 'a']--;
            // If a count goes negative, t has a character that s doesn't
            if (counts[c - 'a'] < 0) {
                return false;
            }
        }
        
        return true;
    }
};
Approach 2: Sorting

C++

#include <string>
#include <algorithm>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        // Sort both strings
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());
        
        // If the sorted strings are identical, they are anagrams
        return s == t;
    }
};
📈 Time & Space Complexity
Approach              Time Complexity   Space Complexity
Frequency Counting    O(N)              O(1)
Sorting               O(N log N)        O(1) or O(N)
N: Length of the strings s and t.

Frequency Counting Space: The space is O(k) where k is the alphabet size (26). Since this is constant, it's O(1).

Sorting Space: The space complexity depends on the implementation of the sort function. It can be O(1) for in-place sorts or up to O(N) for implementations that use extra space.

🏷️ Tags
#HashTable #String #Sorting #LeetCode-Easy