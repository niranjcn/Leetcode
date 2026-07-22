# 🎭 LeetCode 205: Isomorphic Strings

![LeetCode](https://img.shields.io/badge/LeetCode-205-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style-for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Hash%20Table%2C%20String-brightgreen?style-for-the-badge)

---

## 📘 Problem Statement

> Given two strings `s` and `t`, determine if they are isomorphic.
>
> Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.
>
> All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

---

## 📥 Example Inputs

### ✅ Example 1:
```cpp
Input: s = "egg", t = "add"
Output: true
✅ Example 2:
C++

Input: s = "foo", t = "bar"
Output: false
Explanation: 'o' in "foo" cannot map to both 'a' and 'r' in "bar".
✅ Example 3:
C++

Input: s = "paper", t = "title"
Output: true
📌 Constraints
1 <= s.length <= 5 * 10^4

t.length == s.length

s and t consist of any valid ascii character.

💡 Pattern & Approach
This problem is about validating a character mapping between two strings. The key is to ensure the mapping is one-to-one and consistent throughout the strings. A hash map (or an array for a fixed character set) is the perfect tool for this.

Two Hash Maps (to check the bidirectional mapping)

Two Arrays (an optimized version for ASCII characters)

🔍 The Logic
🔹 Approach 1: Two Hash Maps (Bidirectional Check)
To be isomorphic, the mapping must work in both directions without contradictions.

s[i] must always map to t[i].

No other character s[j] can map to t[i].

We can enforce this by using two maps: one for the s -> t mapping and one for the t -> s mapping.

Initialize

Create two hash maps: s_to_t and t_to_s.

Iterate and Compare

Loop through both strings from left to right.

Check s -> t Mapping

If s[i] is already in s_to_t, check if its existing mapping matches t[i]. If not, return false.

Check t -> s Mapping

If t[i] is already in t_to_s, check if its existing mapping matches s[i]. If not, it means t[i] is already mapped from a different character in s. Return false.

Create Mapping

If both checks pass, store the new mapping in both maps.

Return Result

If the loop finishes without contradictions, return true.

🔹 Approach 2: Two Arrays (Optimized Mapping)
Since the characters are ASCII, we can use fixed-size arrays (size 256) instead of hash maps for better performance. The logic is slightly different but achieves the same goal.

Initialize

Create two arrays, map_s and map_t, of size 256, initialized to 0.

Iterate

Loop through the strings.

Check Mapping Consistency

At each character s[i] and t[i], check if map_s[s[i]] is equal to map_t[t[i]].

If they are not equal, it means one character was previously mapped while the other wasn't, or they were mapped to different characters. This is a contradiction. Return false.

Establish Mapping

If the values are equal, it means either both characters are new or they were previously mapped to each other.

We "stamp" them with a unique value (e.g., i + 1) to link them: map_s[s[i]] = i + 1; and map_t[t[i]] = i + 1;.

Return Result

If the loop completes, the mapping is consistent. Return true.

🏃‍♂️ Dry Run Example (Approach 1)
Given:
s = "paper", t = "title"

i	s[i]	t[i]	s_to_t	t_to_s	Action
0	'p'	't'	{}	{}	New. Map p->t, t->p.
1	'a'	'i'	{'p':'t'}	{'t':'p'}	New. Map a->i, i->a.
2	'p'	't'	{'p':'t', 'a':'i'}	{'t':'p', 'i':'a'}	'p' exists, maps to 't'. OK.
3	'e'	'l'	{'p':'t', 'a':'i'}	{'t':'p', 'i':'a'}	New. Map e->l, l->e.
4	'r'	'e'	{'p':'t',..,'e':'l'}	{'t':'p',..,'l':'e'}	New. Map r->e, e->r.

Export to Sheets
✅ Conclusion: The loop completed with no contradictions. Return true.

💻 C++ Code
Approach 1: Two Hash Maps

C++

#include <string>
#include <unordered_map>

class Solution {
public:
    bool isIsomorphic(std::string s, std::string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        std::unordered_map<char, char> s_to_t;
        std::unordered_map<char, char> t_to_s;

        for (int i = 0; i < s.length(); i++) {
            char char_s = s[i];
            char char_t = t[i];

            // Check s->t mapping
            if (s_to_t.count(char_s) && s_to_t[char_s] != char_t) {
                return false;
            }
            // Check t->s mapping
            if (t_to_s.count(char_t) && t_to_s[char_t] != char_s) {
                return false;
            }

            // Establish the bidirectional mapping
            s_to_t[char_s] = char_t;
            t_to_s[char_t] = char_s;
        }
        
        return true;
    }
};
Approach 2: Two Arrays

C++

#include <string>
#include <vector>

class Solution {
public:
    bool isIsomorphic(std::string s, std::string t) {
        // ASCII characters can be mapped using arrays of size 256.
        std::vector<int> map_s(256, 0);
        std::vector<int> map_t(256, 0);

        for (int i = 0; i < s.length(); i++) {
            // If the mapping "stamps" don't match, they are not isomorphic.
            if (map_s[s[i]] != map_t[t[i]]) {
                return false;
            }

            // Stamp both characters with the same unique value (i+1).
            map_s[s[i]] = i + 1;
            map_t[t[i]] = i + 1;
        }

        return true;
    }
};
📈 Time & Space Complexity
Approach           Time Complexity   Space Complexity
Two Hash Maps      O(N)              O(k)
Two Arrays         O(N)              O(1)
N: Length of the strings.

k: Number of unique characters in the strings.

Space Complexity: The space for both approaches is proportional to the size of the character set. Since ASCII has a fixed size (256), the space complexity is technically constant, O(1).

🏷️ Tags
#HashTable #String #LeetCode-Easy