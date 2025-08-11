# 📏 LeetCode 209: Minimum Size Subarray Sum

![LeetCode](https://img.shields.io/badge/LeetCode-209-blue?style=for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Sliding%20Window%2C%20Array-brightgreen?style=for-the-badge)

---

## 📘 Problem Statement

> Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a **subarray** whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

---

## 📥 Example Inputs

### ✅ Example 1:

**Input:**
```
target = 7, nums = [2,3,1,2,4,3]
Output:

C++

2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```
---
```
✅ Example 2:
Input:
target = 4, nums = [1,4,4]
Output:
1
```
---


✅ Example 3:
```
Input:
target = 11, nums = [1,1,1,1,1,1,1,1]
Output:
0
```
---
📌 Constraints
1 <= target <= 10^9

1 <= nums.length <= 10^5

1 <= nums[i] <= 10^4

---

💡 Pattern & Approach (O(n) Solution)
This problem is a classic application of the Sliding Window technique. This pattern is highly efficient for finding a minimum or maximum subarray that satisfies a specific condition.

🔍 The Logic
We maintain a "window" (a subarray) defined by left and right pointers. We expand the window to find a valid sum and then shrink it to find the minimal length.

Initialize:

left pointer at 0.

sum of the current window at 0.

minLen to a very large value (INT_MAX) to track the minimum length.

Expand Window: Use a right pointer to iterate through the array. Add nums[right] to sum.

Check & Shrink Window: Once sum >= target, we have a valid window. Now, we must find the smallest possible length for this window.

Update minLen with the current window length (right - left + 1).

Shrink the window from the left by subtracting nums[left] from sum and incrementing left.

Keep shrinking as long as sum remains >= target, updating minLen each time.

Result: After the loop, if minLen hasn't changed from INT_MAX, no solution was found; return 0. Otherwise, return minLen.

🏃‍♂️ Dry Run Example
Let's trace the sliding window for target = 7, nums = [2,3,1,2,4,3].
Initial State: left = 0, sum = 0, minLen = ∞

right	nums[right]	sum	sum >= 7?	Action	Window Len	minLen	left
0	2	2	No	Expand	-	∞	0
1	3	5	No	Expand	-	∞	0
2	1	6	No	Expand	-	∞	0
3	2	8	Yes	1. Update minLen<br/>2. Shrink (sum -= nums[0])	4	4	1
6	No	while loop ends	-	4	1
4	4	10	Yes	1. Update minLen<br/>2. Shrink (sum -= nums[1])	4	4	2
7	Yes	1. Update minLen<br/>2. Shrink (sum -= nums[2])	3	3	3
6	No	while loop ends	-	3	3
5	3	9	Yes	1. Update minLen<br/>2. Shrink (sum -= nums[3])	3	3	4
7	Yes	1. Update minLen<br/>2. Shrink (sum -= nums[4])	2	2	5
3	No	while loop ends	-	2	5

Export to Sheets
Final Answer: 2

---

💻 C++ Code (O(n) Solution)
C++
```
#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    int minSubArrayLen(int target, std::vector<int>& nums) {
        int left = 0;
        long long sum = 0;
        int minLen = INT_MAX;

        // Iterate through nums with the right pointer to expand the window
        for (int right = 0; right < nums.size(); right++) {
            sum += nums[right];

            // Once the sum is valid, shrink the window from the left
            // to find the smallest possible length.
            while (sum >= target) {
                // Update the minimum length found so far
                minLen = std::min(minLen, right - left + 1);

                // Shrink the window by moving the left pointer
                sum -= nums[left];
                left++;
            }
        }

        // If minLen was never updated, it means no valid subarray was found
        return (minLen == INT_MAX) ? 0 : minLen;
    }
};
```
---
📈 Time & Space Complexity
Complexity	Value	Justification
Time	O(n)	Each element is visited at most twice: once by the right pointer and once by the left pointer. This gives a linear time complexity.
Space	O(1)	We use a constant amount of extra space for pointers and the sum, regardless of the input size.

---


❓ Follow-up: O(n
logn) Solution
The problem asks for an alternate O(n
logn) solution. This can be achieved with Prefix Sums + Binary Search.

Create Prefix Sums: Build a prefix array where prefix[i] is the sum of nums from 0 to i-1.

Iterate and Search: Loop through the prefix array from i = 1 to n. For each prefix[i], we need to find an earlier index j such that prefix[i] - prefix[j] >= target.

Binary Search: This condition can be rewritten as prefix[j] <= prefix[i] - target. We can use binary search on the prefix array (from index 0 to i-1) to efficiently find the required j. This search takes O(
logn) time.

Since we perform this search for each of the n elements, the total time complexity becomes O(n
logn).
---
🏷️ Tags
#SlidingWindow #TwoPointers #Array #BinarySearch #LeetCode-Medium
