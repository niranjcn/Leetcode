# ✅ LeetCode 20: Valid Parentheses

![LeetCode](https://img.shields.io/badge/LeetCode-20-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style-for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Stack%2C%20String-brightgreen?style-for-the-badge)

---

## 📘 Problem Statement

> Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid.
>
> An input string is valid if:
> 1.  Open brackets must be closed by the same type of brackets.
> 2.  Open brackets must be closed in the correct order.
> 3.  Every close bracket has a corresponding open bracket of the same type.

---

## 📥 Example Inputs

### ✅ Example 1:
```cpp
Input: s = "()"
Output: true
✅ Example 2:
C++

Input: s = "()[]{}"
Output: true
✅ Example 3:
C++

Input: s = "(]"
Output: false
✅ Example 4:
C++

Input: s = "([])"
Output: true
✅ Example 5:
C++

Input: s = "([)]"
Output: false
📌 Constraints
1 <= s.length <= 10^4

s consists of parentheses only '()[]{}'.

💡 Pattern & Approach
This problem is a classic application of the Stack data structure. A stack follows a Last-In, First-Out (LIFO) principle, which perfectly mirrors the way nested parentheses must be resolved: the most recently opened bracket must be the first one to be closed.

Stack-Based Matching (The canonical and most efficient approach)

🔍 The Logic
🔹 Approach: Stack-Based Matching
We iterate through the string, using a stack to keep track of the open brackets we've encountered.

Initialize a Stack

Create an empty stack of characters.

Iterate Through String

For each character c in the string:

Handle Opening Brackets

If c is an opening bracket ((, [, {), push it onto the stack. We are "opening" a new scope that needs to be closed later.

Handle Closing Brackets

If c is a closing bracket (), ], }):

Check for an opener: First, check if the stack is empty. If it is, we have a closing bracket with no matching opener, so the string is invalid. Return false.

Pop and Compare: If the stack is not empty, pop the top element. This is the most recently opened bracket. Check if it correctly matches the current closing bracket.

Mismatch: If c is ) but the popped character is not (, or } not with {, etc., then the order is incorrect. Return false.

Final Check

After the loop finishes, the string is valid only if the stack is empty.

An empty stack means every opening bracket found its matching closing bracket.

If the stack is not empty, it means there are unclosed opening brackets.

🏃‍♂️ Dry Run Example
Given:
s = "([])"

Character	Action	Stack State (Bottom -> Top)
(	It's an opening bracket.	Push (.
]	It's a closing bracket. Stack is not empty.	Pop. Top is [, which matches ].

Export to Sheets
Final Step: The loop finishes. The stack is empty.
✅ Conclusion: Return true.

💻 C++ Code
C++

#include <string>
#include <stack>

class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> st;
        
        for (char c : s) {
            // If it's an opening bracket, push it onto the stack.
            if (c == '(' || c == '[' || c == '{') {
                st.push(c);
            } 
            // If it's a closing bracket...
            else {
                // ...but the stack is empty, there's no opener. Invalid.
                if (st.empty()) {
                    return false;
                }
                
                // Get the last opened bracket.
                char top = st.top();
                st.pop();
                
                // Check if the closer matches the opener.
                if ((c == ')' && top != '(') ||
                    (c == ']' && top != '[') ||
                    (c == '}' && top != '{')) {
                    return false; // Mismatch.
                }
            }
        }
        
        // If the stack is empty at the end, all brackets were matched.
        return st.empty();
    }
};
📈 Time & Space Complexity
Approach           Time Complexity   Space Complexity
Stack Matching     O(N)              O(N)
N: Length of the input string s.

Time Complexity: We iterate through the string once, and each stack operation (push, pop) takes constant time on average.

Space Complexity: In the worst-case scenario (e.g., a string of all opening brackets like "((((..."), the stack will hold all N characters.

🏷️ Tags
#Stack #String #LeetCode-Easy