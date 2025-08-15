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

**Input:**
```cpp
matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output:

C++

[1,2,3,6,9,8,7,4,5]
✅ Example 2:
Input:

C++

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output:

C++

[1,2,3,4,8,12,11,10,9,5,6,7]
📌 Constraints
m == matrix.length

n == matrix[i].length

1 <= m, n <= 10

-100 <= matrix[i][j] <= 100

💡 Pattern & Approach
The problem asks us to simulate a spiral traversal of a matrix. The most intuitive way to handle this is a Layer-by-Layer Simulation using boundary pointers. We can think of this as peeling an onion from the outside in.

🔍 The Logic
We'll define four pointers to represent the boundaries of the current layer we are traversing: top, bottom, left, and right. In each iteration of a loop, we will traverse the four sides of the current layer and then shrink the boundaries inward to process the next layer.

Initialize Boundaries:

top = 0 (the first row)

bottom = m - 1 (the last row)

left = 0 (the first column)

right = n - 1 (the last column)

Loop While Boundaries Are Valid: Continue the process as long as there's a valid layer to traverse, i.e., top <= bottom and left <= right.

Traverse the Four Sides of the Current Layer:

Go Right (Top Row): Iterate from left to right along the top row, adding each element to our result. After this, we've processed the top row, so we increment top.

Go Down (Right Column): Iterate from the new top to bottom along the right column. Then, decrement right.

Go Left (Bottom Row): Iterate from the new right back to left along the bottom row. Then, decrement bottom. This step requires a check (if (top <= bottom)) to handle matrices that are just a single row or column.

Go Up (Left Column): Iterate from the new bottom back to top along the left column. Then, increment left. This also requires a check (if (left <= right)).

Repeat: The loop continues, with the boundaries shrinking inward, until they cross each other.

🏃‍♂️ Dry Run Example
Let's trace matrix = [[1,2,3],[4,5,6],[7,8,9]].
Initial State: top=0, bottom=2, left=0, right=2, result=[]

Iteration	Action	Boundaries after Action	Result
1	Go Right (row 0)	top=1	[1, 2, 3]
Go Down (col 2)	right=1	[1, 2, 3, 6, 9]
Go Left (row 2)	bottom=1	[1, 2, 3, 6, 9, 8, 7]
Go Up (col 0)	left=1	[1, 2, 3, 6, 9, 8, 7, 4]
2	Go Right (row 1)	top=2	[1, 2, 3, 6, 9, 8, 7, 4, 5]
Go Down (col 1)	right=0	(Loop i=2..1 doesn't run)
Go Left (row 1)	bottom=0	(Loop j=0..1 doesn't run)
Go Up (col 1)	left=2	(Loop i=0..2 doesn't run)
End Condition: The while loop condition top <= bottom (2 <= 1) is now false. The process terminates.
Final Answer: [1, 2, 3, 6, 9, 8, 7, 4, 5]

💻 C++ Code
C++

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
📈 Time & Space Complexity
Complexity	Value	Justification
Time	O(m
timesn)	We visit every element in the matrix exactly once.
Space	O(1)	The space used by the algorithm itself (for the boundary pointers) is constant. If we consider the output result vector, the space complexity is O(m
timesn), as it stores all elements.
🏷️ Tags
#Array #Matrix #Simulation #LeetCode-Medium