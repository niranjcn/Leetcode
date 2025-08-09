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

## 💡 Pattern & Approach
This problem can be solved efficiently using the **Two-Pointer Technique** combined with a **Greedy Shrinking** strategy.

---

## 🔍 The Logic

1. **Initialize Pointers**  
   Set two pointers:
   - `i` at the start (`0`)
   - `j` at the end (`n-1`)

2. **Calculate Area**  
   At each step:
   - **Width** = `j - i`
   - **Height** = `min(height[i], height[j])`
   - **Area** = `width × height`
   
Area = (j - i) × min(height[i], height[j])

markdown
Copy
Edit

3. **Update Maximum**  
Keep track of `maxcap` — the maximum area found so far.

4. **Move the Pointer (Greedy Choice)**  
- If `height[i] < height[j]`, increment `i` (move left pointer rightward).
- Else, decrement `j` (move right pointer leftward).  

This works because reducing the taller side can't yield a larger area; we must try to find a taller boundary.

5. **Termination**  
Repeat until `i >= j`.  
The value in `maxcap` will be the final answer.

---

## 🏃‍♂️ Dry Run Example

Given:
height = [1,8,6,2,5,4,8,3,7]

python
Copy
Edit

| i  | j  | height[i] | height[j] | width | min height | area | maxcap |
|----|----|-----------|-----------|-------|------------|------|--------|
| 0  | 8  | 1         | 7         | 8     | 1          | 8    | 8      |
| 1  | 8  | 8         | 7         | 7     | 7          | 49   | 49     |
| 1  | 7  | 8         | 3         | 6     | 3          | 18   | 49     |
| 1  | 6  | 8         | 8         | 5     | 8          | 40   | 49     |
| 1  | 5  | 8         | 4         | 4     | 4          | 16   | 49     |
| 1  | 4  | 8         | 5         | 3     | 5          | 15   | 49     |
| 1  | 3  | 8         | 2         | 2     | 2          | 4    | 49     |
| 1  | 2  | 8         | 6         | 1     | 6          | 6    | 49     |

**Final Answer:** `49`


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
