# 🏺 LeetCode 11: Container With Most Water

![LeetCode](https://img.shields.io/badge/LeetCode-11-blue?style=for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)

---

## 📘 Problem Statement

> You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`.
>
> Find two lines that, together with the x-axis, form a container that can hold the most water.
>
> Return the **maximum amount of water** a container can store.
>
> **Note:** You may not slant the container.



---

## 📥 Example Inputs

### ✅ Example 1:

**Input:**
```
height = [1,8,6,2,5,4,8,3,7]
Output:49
```
Explanation: The vertical lines are represented by the array [1,8,6,2,5,4,8,3,7]. The maximum area of water the container can hold is 49 (achieved between the line at index 1 with height 8 and the line at index 8 with height 7).

✅ Example 2:
Input:

```
height = [1,1]
Output:1
```
---
📌 Constraints
n == height.length

2 <= n <= 10^5

0 <= height[i] <= 10^4

---

💡 Pattern & Approach
This problem can be efficiently solved using the Two-Pointer Technique with a Greedy Shrinking strategy.

The Logic
The core idea is to start with the widest possible container and iteratively shrink it, always aiming for a potentially larger area.

Initialize Pointers: Start with two pointers, i at the beginning of the array (0) and j at the end (n-1).

Calculate Area: In each step, calculate the area formed by the lines at i and j. The width is j - i, and the height is limited by the shorter of the two lines.

$$$$$$Area = (j - i) \\times \\min(height[i], height[j]) $$
$$$$

Update Maximum: Keep track of the maximum area found so far (maxcap). If the current area is greater, update maxcap.

Move the Pointer: This is the key greedy step. To potentially find a larger area, we must increase the height of our container. Since the width (j - i) is guaranteed to decrease, our only hope for a larger area is a taller bounding line.

If height[i] < height[j], we move the left pointer i one step to the right (i++). We do this because moving the taller pointer j inward would definitely result in a smaller or equal area (as the width decreases and the height is still limited by height[i]).

Otherwise, if height[j] <= height[i], we move the right pointer j one step to the left (j--).

Termination: Continue this process until the pointers meet (i >= j). The value stored in maxcap will be the answer.

🏃‍♂️ Dry Run
Let's trace the algorithm with height = [1,8,6,2,5,4,8,3,7]:

i	j	height[i]	height[j]	width	min height	area	maxcap
0	8	1	7	8	1	8	8
1	8	8	7	7	7	49	49
1	7	8	3	6	3	18	49
1	6	8	8	5	8	40	49
1	5	8	4	4	4	16	49
1	4	8	5	3	5	15	49
1	3	8	2	2	2	4	49
1	2	8	6	1	6	6	49

Export to Sheets
The loop terminates as i would become 2, making i == j. The final result is 49.

---

💻 C++ Code
C++
```
class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size() - 1;
        int maxcap = 0; // Initialize with 0, as area cannot be negative

        while (i < j) {
            // Calculate the area with the current pair of lines
            int current_area = (j - i) * min(height[i], height[j]);
            
            // Update the maximum capacity found so far
            maxcap = max(current_area, maxcap);
            
            // Move the pointer pointing to the shorter line
            if (height[i] < height[j]) {
                i++;
            } else {
                j--;
            }
        }
        return maxcap;
    }
};
```
---
```
📈 Time & Space Complexity
Complexity	Value
Time	O(n)
Space	O(1)
```

Export to Sheets
Since the two pointers i and j traverse the array only once, the time complexity is linear. No extra data structures are used, so the space complexity is constant.

🏷️ Tags
#TwoPointers #Greedy #Array #LeetCode-Medium #Math
