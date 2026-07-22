# 📜 LeetCode 383: Ransom Note

![LeetCode](https://img.shields.io/badge/LeetCode-383-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style-for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Hash%20Table%2C%20String-brightgreen?style-for-the-badge)

---

## 📘 Problem Statement

> Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.
>
> Each letter in `magazine` can only be used once in `ransomNote`.

---

## 📥 Example Inputs

### ✅ Example 1:
```cpp
Input: ransomNote = "a", magazine = "b"
Output: false
✅ Example 2:
C++

Input: ransomNote = "aa", magazine = "ab"
Output: false
✅ Example 3:
C++

Input: ransomNote = "aa", magazine = "aab"
Output: true
📌 Constraints
1 <= ransomNote.length, magazine.length <= 10^5

ransomNote and magazine consist of lowercase English letters.

💡 Pattern & Approach
This problem is a classic frequency counting problem. The goal is to verify if we have enough of each required character in the magazine to build the ransomNote. This is a perfect use case for a hash map or a simple array as a frequency counter.

Frequency Counting (Single Array: Build & Consume)

Frequency Counting (Two Arrays: Build & Compare)

🔍 The Logic
🔹 Approach 1: Single Array Frequency Count (Build & Consume)
This is the most efficient method. We first count all available characters in the magazine. Then, we iterate through the ransomNote, "consuming" the characters from our count. If we try to consume a character that we don't have, it's impossible.

Initialize Counter

Create an integer array count of size 26 (for 'a' through 'z'), initialized to all zeros.

Count Magazine Characters

Iterate through the magazine string. For each character ch, increment its corresponding counter: count[ch - 'a']++.

Check Ransom Note

Iterate through the ransomNote string.

Decrement and Validate

For each character ch, check if its count is already zero (count[ch - 'a'] == 0).

If it is zero, we've run out of that letter. Return false.

If it's not zero, decrement the count to mark one as "used".

Return Result

If the ransomNote loop completes, we had enough characters. Return true.

🔹 Approach 2: Two Array Frequency Count (Build & Compare)
This is a slightly different implementation of the same idea. We build frequency maps for both strings first, then compare them.

Initialize Two Counters

Create two integer arrays of size 26, noteCount and magCount.

Count Frequencies

Populate noteCount by iterating through ransomNote.

Populate magCount by iterating through magazine.

Compare Counts

Loop from i = 0 to 25.

For each character, check if magCount[i] < noteCount[i].

Check for Insufficiency

If the magazine has fewer of any required character, return false.

Return Result

If the loop completes, the magazine has sufficient characters. Return true.

🏃‍♂️ Dry Run Example (Approach 1)
Given:
ransomNote = "aa", magazine = "aab"

Action	Character	count['a']	count['b']	Note
Initialize	-	0	0	count array is all zeros.
Scan Magazine	'a'	1	0	
'a'	2	0	
'b'	2	1	Magazine scan complete.
Scan Note	'a'	1	1	count['a'] was > 0. Decrement.
'a'	0	1	count['a'] was > 0. Decrement.
End of Note	-	0	1	Loop finished.

Export to Sheets
✅ Conclusion: The loop completed successfully, so we return true.

💻 C++ Code
Approach 1: Single Array (Build & Consume)

C++

#include <string>
#include <vector>

class Solution {
public:
    bool canConstruct(std::string ransomNote, std::string magazine) {
        // Array to store frequency of characters in the magazine.
        std::vector<int> count(26, 0);
        
        // Populate the frequency count from the magazine.
        for (char ch : magazine) {
            count[ch - 'a']++;
        }
        
        // Check if the ransom note can be constructed.
        for (char ch : ransomNote) {
            // If a required character is not available (count is 0), return false.
            if (count[ch - 'a'] == 0) {
                return false;
            }
            // Decrement the count for the used character.
            count[ch - 'a']--;
        }
        
        return true;
    }
};
Approach 2: Two Arrays (Build & Compare)

C++

#include <string>
#include <vector>

class Solution {
public:
    bool canConstruct(std::string ransomNote, std::string magazine) {
        // Create frequency maps for both strings.
        std::vector<int> noteCount(26, 0);
        std::vector<int> magCount(26, 0);

        for (char ch : ransomNote) {
            noteCount[ch - 'a']++;
        }
        for (char ch : magazine) {
            magCount[ch - 'a']++;
        }

        // Compare the frequency maps.
        for (int i = 0; i < 26; i++) {
            // If magazine has fewer characters than needed for the note.
            if (magCount[i] < noteCount[i]) {
                return false;
            }
        }

        return true;
    }
};
📈 Time & Space Complexity
Approach           Time Complexity   Space Complexity
Single Array       O(M + N)          O(1)
Two Arrays         O(M + N)          O(1)
M: Length of the magazine string.

N: Length of the ransomNote string.

Space Complexity: The space is O(k) where k is the number of characters in the alphabet (26). Since k is a fixed constant, the space complexity is O(1).

🏷️ Tags
#HashTable #String #Counting #LeetCode-Easy