# 🌀 LeetCode 54: Spiral Matrix

![LeetCode](https://img.shields.io/badge/LeetCode-54-blue?style=for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Array%2C%20Matrix%2C%20Simulation-brightgreen?style=for-the-badge)

---

## 📘 Problem Statement

> Given an `m x n` matrix, return all elements of the matrix in spiral order.

---

## 📥 Example Inputs

### ✅ Example 1:
```
**Input:**

matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output:
[1,2,3,6,9,8,7,4,5]
```
---

✅ Example 2:
```
Input:
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
output:[1,2,3,4,8,12,11,10,9,5,6,7]
```
---

📌 Constraints
m == matrix.length

n == matrix[i].length

1 <= m, n <= 10

-100 <= matrix[i][j] <= 100

---

## 💡 Pattern & Approach
The problem asks us to simulate a **spiral traversal of a matrix**.  
The most intuitive way to handle this is a **Layer-by-Layer Simulation** using boundary pointers.  
Think of it as peeling an onion from the outside in.

---

## 🔍 The Logic
We define **four pointers** to represent the boundaries of the current layer:

- `top` = 0 (the first row)  
- `bottom` = m - 1 (the last row)  
- `left` = 0 (the first column)  
- `right` = n - 1 (the last column)  

---

**Algorithm Steps:**

1. **Loop While Boundaries Are Valid:**  
   Continue as long as `top <= bottom` and `left <= right`.

2. **Traverse the Four Sides:**
   - **Go Right (Top Row):**  
     From `left` to `right` along `top` row → increment `top`.
   - **Go Down (Right Column):**  
     From `top` to `bottom` along `right` column → decrement `right`.
   - **Go Left (Bottom Row):**  
     From `right` to `left` along `bottom` row → decrement `bottom`.  
     _(Check if `top <= bottom` before doing this step.)_
   - **Go Up (Left Column):**  
     From `bottom` to `top` along `left` column → increment `left`.  
     _(Check if `left <= right` before doing this step.)_

3. **Repeat:**  
   Shrink boundaries inward and process the next layer.

4. **Stop Condition:**  
   Loop ends when boundaries cross.

---

## 🏃‍♂️ Dry Run Example
Let's trace:

`matrix = [[1,2,3],[4,5,6],[7,8,9]]`

Initial:  
`top=0, bottom=2, left=0, right=2, result=[]`

| Iteration | Action                              | Boundaries After Action     | Result                           |
|-----------|-------------------------------------|------------------------------|-----------------------------------|
| **1**     | Go Right (row 0)                    | `top = 1`                    | [1, 2, 3]                         |
|           | Go Down (col 2)                     | `right = 1`                  | [1, 2, 3, 6, 9]                   |
|           | Go Left (row 2)                     | `bottom = 1`                  | [1, 2, 3, 6, 9, 8, 7]             |
|           | Go Up (col 0)                       | `left = 1`                   | [1, 2, 3, 6, 9, 8, 7, 4]          |
| **2**     | Go Right (row 1)                    | `top = 2`                    | [1, 2, 3, 6, 9, 8, 7, 4, 5]       |
|           | Go Down (col 1) _(no elements)_     | `right = 0`                  | (No change)                       |
|           | Go Left (row 1) _(no elements)_     | `bottom = 0`                  | (No change)                       |
|           | Go Up (col 1) _(no elements)_       | `left = 2`                   | (No change)                       |

**End Condition:** `top <= bottom` is now false → loop stops.

✅ **Final Answer:** `[1, 2, 3, 6, 9, 8, 7, 4, 5]`


💻 C++ Code
```
#include <vector>

class Solution {
public:
    std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        
        // Initialize boundary pointers
        int top = 0, bottom = m - 1;
        int left = 0, right = n - 1;
        
        std::vector<int> result;

        // Loop until the boundaries cross
        while (top <= bottom && left <= right) {
            // 1. Traverse the top row from left to right
            for (int j = left; j <= right; j++) {
                result.push_back(matrix[top][j]);
            }
            top++;

            // 2. Traverse the right column from top to bottom
            for (int i = top; i <= bottom; i++) {
                result.push_back(matrix[i][right]);
            }
            right--;

            // 3. Traverse the bottom row from right to left (if it's a valid row)
            if (top <= bottom) {
                for (int j = right; j >= left; j--) {
                    result.push_back(matrix[bottom][j]);
                }
                bottom--;
            }

            // 4. Traverse the left column from bottom to top (if it's a valid column)
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    result.push_back(matrix[i][left]);
                }
                left++;
            }
        }
        return result;
    }
};
```
---

📈 Time & Space Complexity
Complexity	Value	Justification
Time	O(m
timesn)	We visit every element in the matrix exactly once.
Space	O(1)	The space used by the algorithm itself (for the boundary pointers) is constant. If we consider the output result vector, the space complexity is O(m
timesn), as it stores all elements.
---
🏷️ Tags
#Array #Matrix #Simulation #LeetCode-Medium
