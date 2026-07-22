# 🧩 LeetCode 290: Word Pattern

![LeetCode](https://img.shields.io/badge/LeetCode-290-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style-for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Hash%20Table%2C%20String-brightgreen?style-for-the-badge)

---

## 📘 Problem Statement

> Given a `pattern` and a string `s`, find if `s` follows the same pattern.
>
> Here **follow** means a full match, such that there is a **bijection** (a one-to-one mapping) between a letter in `pattern` and a non-empty word in `s`.

---

## 📥 Example Inputs

### ✅ Example 1:
```cpp
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
✅ Example 2:
C++

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Explanation: pattern[3] which is 'a' should map to "dog", but s has "fish" at that position.
✅ Example 3:
C++

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Explanation: pattern[0] ('a') maps to "dog", but pattern[1] ('a') cannot also map to "cat".

📌 Constraints
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

💡 Pattern & Approach
This problem is a direct test of a bijection (a one-to-one and onto mapping) between two sets: the characters of the pattern and the words of the string s. This is a classic hash map problem, very similar to Isomorphic Strings.

Two Hash Maps (to enforce the bidirectional mapping)

Canonical Representation (to transform both inputs into a common format)

🔍 The Logic
🔹 Approach 1: Two Hash Maps (Bidirectional Check)
To ensure a bijection, we need to verify the mapping in both directions simultaneously. A character must always map to the same word, and a word must always be mapped from the same character.

Pre-processing

Split the string s into a vector of words. A stringstream is perfect for this.

Check if the length of the pattern and the number of words are equal. If not, return false.

Initialize

Create two hash maps: char_to_word and word_to_char.

Iterate and Compare

Loop through the pattern characters and words at the same index i.

Check Mappings

char -> word: Check if pattern[i] already exists in char_to_word. If it does, its mapped value must equal words[i]. If not, the pattern is broken.

word -> char: Check if words[i] already exists in word_to_char. If it does, its mapped value must equal pattern[i]. If not, the pattern is broken.

Create Mapping

If both checks pass, store the new mapping in both maps: char_to_word[pattern[i]] = words[i] and word_to_char[words[i]] = pattern[i].

Return Result

If the loop completes without contradictions, return true.

🔹 Approach 2: Canonical Representation
An alternative is to transform both the pattern and the words into a common, canonical form. If their forms are identical, they match. A simple canonical form is a sequence of the first-seen index of each element.

Pre-processing

Split s into words and check for length mismatch.

Transform Pattern

Create an integer vector. For each character in pattern, find the index where it first appeared and add that index to the vector. E.g., "abba" -> [0, 1, 1, 0].

Transform Words

Do the same for the words in s. E.g., "dog cat cat dog" -> [0, 1, 1, 0].

Compare

If the two generated integer vectors are identical, the pattern holds. Return true.

🏃‍♂️ Dry Run Example (Approach 1)
Given:
pattern = "abba", s = "dog cat cat dog"
Words: ["dog", "cat", "cat", "dog"]

i	pattern[i]	word	char_to_word	word_to_char	Action / Check
0	'a'	"dog"	{}	{}	New. Map a->"dog", "dog"->a.
1	'b'	"cat"	{'a':"dog"}	{"dog":'a'}	New. Map b->"cat", "cat"->b.
2	'b'	"cat"	{'a':"d",'b':"c"}	{"d":'a',"c":'b'}	'b' exists, maps to "cat". OK.
3	'a'	"dog"	{'a':"d",'b':"c"}	{"d":'a',"c":'b'}	'a' exists, maps to "dog". OK.

Export to Sheets
✅ Conclusion: The loop completes with no contradictions. Return true.

💻 C++ Code
Approach 1: Two Hash Maps

C++

#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>

class Solution {
public:
    bool wordPattern(std::string pattern, std::string s) {
        // 1. Pre-processing: Split s into words
        std::vector<std::string> words;
        std::string word;
        std::stringstream ss(s);
        while (ss >> word) {
            words.push_back(word);
        }

        // 2. Length Check
        if (pattern.length() != words.size()) {
            return false;
        }

        // 3. Initialize two maps for bidirectional check
        std::unordered_map<char, std::string> char_to_word;
        std::unordered_map<std::string, char> word_to_char;

        // 4. Iterate and Compare
        for (int i = 0; i < pattern.length(); i++) {
            char p_char = pattern[i];
            std::string s_word = words[i];

            // 5. Check char -> word mapping
            if (char_to_word.count(p_char) && char_to_word[p_char] != s_word) {
                return false;
            }
            // 6. Check word -> char mapping
            if (word_to_char.count(s_word) && word_to_char[s_word] != p_char) {
                return false;
            }

            // 7. Create Mapping
            char_to_word[p_char] = s_word;
            word_to_char[s_word] = p_char;
        }

        return true;
    }
};
📈 Time & Space Complexity
Approach           Time Complexity   Space Complexity
Two Hash Maps      O(P + S)          O(Up + Uw)
P: Length of the pattern.

S: Length of the string s.

Up: Number of unique characters in pattern.

Uw: Number of unique words in s.

The time complexity includes parsing the string s and then iterating through the pattern. The space complexity depends on the number of unique mappings stored.

🏷️ Tags
#HashTable #String #LeetCode-Easy