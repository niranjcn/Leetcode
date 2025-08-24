# 😊 LeetCode 202: Happy Number

![LeetCode](https://img.shields.io/badge/LeetCode-202-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style-for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Hash%20Table%2C%20Math%2C%20Two%20Pointers-brightgreen?style-for-the-badge)

---

## 📘 Problem Statement

> Write an algorithm to determine if a number `n` is **happy**.
>
> A **happy number** is a number defined by the following process:
> - Starting with any positive integer, replace the number by the sum of the squares of its digits.
> - Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
> - Those numbers for which this process **ends in 1** are happy.
>
> Return `true` if `n` is a happy number, and `false` if not.

---

## 📥 Example Inputs

### ✅ Example 1:
```cpp
Input: n = 19
Output: true
Explanation:

1² + 9² = 1 + 81 = 82

8² + 2² = 64 + 4 = 68

6² + 8² = 36 + 64 = 100

1² + 0² + 0² = 1

✅ Example 2:
C++

Input: n = 2
Output: false
Explanation: 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 ... The sequence enters a cycle and never reaches 1.
📌 Constraints
1 <= n <= 2^31 - 1

💡 Pattern & Approach
The problem states that an unhappy number gets stuck in a cycle. This transforms the problem into a cycle detection problem. We can think of the sequence of numbers as an invisible linked list, where each number points to the next number in the sequence.

Cycle Detection with a Hash Set (Easy to understand, uses extra space)

Cycle Detection with Two Pointers (Floyd's Tortoise and Hare algorithm, space-optimized)

🔍 The Logic
🔹 Approach 1: Cycle Detection with a Hash Set
We keep track of every number we encounter. If we see a number for a second time before reaching 1, we've found a cycle, and the number is not happy.

Initialize

Create a hash set seen to store the numbers encountered so far.

Main Loop

Loop as long as the current number n is not equal to 1.

Check for Cycle

Inside the loop, check if n is already in the seen set.

If yes, a cycle is detected. Return false.

Record and Update

If n is not in the set, add it: seen.insert(n).

Calculate the sum of the squares of the digits of n.

Update n to this new sum.

Return Result

If the loop exits, it's because n became 1. The number is happy, so return true.

🔹 Approach 2: Floyd's Tortoise and Hare (Two Pointers)
This classic cycle-detection algorithm uses two "pointers" moving at different speeds. A "slow" pointer moves one step at a time, and a "fast" pointer moves two steps. If a cycle exists, the fast pointer will eventually lap the slow pointer.

Helper Function

Create a helper function, sumSquareDigits(num), that takes a number and returns the sum of the squares of its digits.

Initialize Pointers

slow = n

fast = n

Move Pointers

In a loop, update the pointers at their respective speeds:

slow = sumSquareDigits(slow);

fast = sumSquareDigits(sumSquareDigits(fast));

Check for Collision

The loop continues until slow == fast.

Return Result

Once the pointers meet, a cycle has been found. If the cycle is at 1 (slow == 1), the number is happy. Otherwise, it's not.

🏃‍♂️ Dry Run Example (Approach 1)
Given:
n = 19

n	seen contains n?	Action	seen State	Next n
19	No	Add 19 to seen.	{19}	82
82	No	Add 82 to seen.	{19, 82}	68
68	No	Add 68 to seen.	{19, 82, 68}	100
100	No	Add 100 to seen.	{19, 82, 68, 100}	1
1	-	Loop terminates as n == 1.	-	-

Export to Sheets
✅ Conclusion: The loop finished by reaching 1. Return true.

💻 C++ Code
Approach 1: Cycle Detection with a Hash Set

C++

#include <unordered_set>

class Solution {
public:
    int getNext(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n = n / 10;
        }
        return sum;
    }

    bool isHappy(int n) {
        std::unordered_set<int> seen;
        while (n != 1 && seen.find(n) == seen.end()) {
            seen.insert(n);
            n = getNext(n);
        }
        return n == 1;
    }
};
Approach 2: Two Pointers (Floyd's Tortoise and Hare)

C++

class Solution {
public:
    int getNext(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n = n / 10;
        }
        return sum;
    }

    bool isHappy(int n) {
        int slow = n;
        int fast = getNext(n);

        while (fast != 1 && slow != fast) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }
        
        return fast == 1;
    }
};
📈 Time & Space Complexity
Approach           Time Complexity   Space Complexity
Hash Set           O(log N)          O(log N)
Two Pointers       O(log N)          O(1)
Why O(log N)? The sum of squares of digits of a number N is much smaller than N. For example, the largest sum for a 3-digit number is 9^2 + 9^2 + 9^2 = 243. The numbers shrink very quickly to a small range where cycles can occur. The number of steps is therefore related to the number of digits, which is log N.

Space Complexity: The Two Pointers approach is superior as it uses constant extra space.

🏷️ Tags
#HashTable #Math #TwoPointers #LeetCode-Easy