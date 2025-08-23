# 🔠 LeetCode 49: Group Anagrams

![LeetCode](https://img.shields.io/badge/LeetCode-49-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style-for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Hash%20Table%2C%20String%2C%20Sorting-brightgreen?style-for-the-badge)

---

## 📘 Problem Statement

> Given an array of strings `strs`, group the **anagrams** together. You can return the answer in any order.
>
> An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

## 📥 Example Inputs

### ✅ Example 1:
```cpp
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
✅ Example 2:
C++

Input: strs = [""]
Output: [[""]]
✅ Example 3:
C++

Input: strs = ["a"]
Output: [["a"]]
📌 Constraints
1 <= strs.length <= 10^4

0 <= strs[i].length <= 100

strs[i] consists of lowercase English letters.

💡 Pattern & Approach
The core idea is to find a canonical representation (a unique key) for all strings that are anagrams of each other. We can then use a hash map to group the strings based on this key.

Categorize by Sorted String (intuitive and easy to implement)

Categorize by Character Count (often more performant)

🔍 The Logic
🔹 Approach 1: Categorize by Sorted String
If two strings are anagrams, they will be identical when their characters are sorted alphabetically. This sorted string serves as a perfect key for our hash map.

Initialize

Create a hash map, map, where the key is a string (the sorted key) and the value is a vector<string> (the group of anagrams).

Iterate Through Strings

For each string str in the input array strs:

Create a copy of str, let's call it key.

Sort key alphabetically.

Group by Key

Add the original str to the vector associated with the key in the map: map[key].push_back(str).

Collect Results

After the loop, the map contains all the grouped anagrams.

Iterate through the map and push each value (the vector<string>) into a final result vector.

🔹 Approach 2: Categorize by Character Count
Instead of sorting, we can generate a key from the frequency of characters. All anagrams will have the exact same character counts.

Initialize

Create a hash map, map, similar to the first approach.

Iterate Through Strings

For each str in strs:

Create a frequency array count of size 26, initialized to zeros.

Populate count by iterating through the characters of str.

Encode Key

Convert the count array into a unique string key. For example, a count for "abb" [1,2,0...] could become a key like "a1b2".

Group by Key

Add the original str to the vector associated with this frequency key.

Collect Results

Extract the grouped anagrams from the map's values.

🏃‍♂️ Dry Run Example (Approach 1)
Given:
strs = ["eat","tea","tan","ate","nat","bat"]

Original String	Sorted Key	Map State (map<string, vector<string>>)
"eat"	"aet"	{"aet": ["eat"]}
"tea"	"aet"	{"aet": ["eat", "tea"]}
"tan"	"ant"	{"aet": [...], "ant": ["tan"]}
"ate"	"aet"	{"aet": ["eat", "tea", "ate"], "ant": [...]}
"nat"	"ant"	{"aet": [...], "ant": ["tan", "nat"]}
"bat"	"abt"	{"aet": [...], "ant": [...], "abt": ["bat"]}
Final Step: Collect the values from the map: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]. (Order may vary).

💻 C++ Code
Approach 1: Categorize by Sorted String

C++

#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        // Map to store groups of anagrams. Key: sorted string, Value: list of anagrams.
        std::unordered_map<std::string, std::vector<std::string>> map;

        for (const std::string& str : strs) {
            // Create the canonical key by sorting the string.
            std::string key = str;
            std::sort(key.begin(), key.end());
            
            // Group the original string under its canonical key.
            map[key].push_back(str);
        }

        // Collect the results from the map.
        std::vector<std::vector<std::string>> result;
        for (const auto& entry : map) {
            result.push_back(entry.second);
        }

        return result;
    }
};
Approach 2: Categorize by Character Count

C++

#include <string>
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> map;

        for (const std::string& str : strs) {
            // Create a frequency count array.
            std::vector<int> count(26, 0);
            for (char c : str) {
                count[c - 'a']++;
            }
            
            // Build the canonical key from the count array.
            std::string key = "";
            for (int i = 0; i < 26; i++) {
                if (count[i] > 0) {
                    key += ('a' + i);
                    key += std::to_string(count[i]);
                }
            }
            
            map[key].push_back(str);
        }

        std::vector<std::vector<std::string>> result;
        for (const auto& entry : map) {
            result.push_back(entry.second);
        }
        
        return result;
    }
};
📈 Time & Space Complexity
Approach              Time Complexity   Space Complexity
Sorted String Key     O(N * K log K)    O(N * K)
Char Count Key        O(N * K)          O(N * K)
N: Number of strings in the input array strs.

K: Maximum length of a string in strs.

Time Complexity: The Character Count approach is generally faster because counting characters (O(K)) is more efficient than sorting them (O(K log K)) for each string.

Space Complexity: In the worst case, every string is unique, and we store all N*K characters in the hash map.

🏷️ Tags
#HashTable #String #Sorting #LeetCode-Medium