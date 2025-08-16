# 🧩 LeetCode 36: Valid Sudoku

![LeetCode](https://img.shields.io/badge/LeetCode-36-blue?style=for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Array%2C%20Hash%20Table%2C%20Matrix-brightgreen?style=for-the-badge)

---

## 📘 Problem Statement

> Determine if a **9 x 9** Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
> 1.  Each row must contain the digits `1-9` without repetition.
> 2.  Each column must contain the digits `1-9` without repetition.
> 3.  Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.
>
> **Note:**
> * A Sudoku board (partially filled) could be valid but is not necessarily solvable.
> * Only the filled cells need to be validated according to the mentioned rules.



---

## 📥 Example Inputs

### ✅ Example 1:

**Input:**
```
board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output:
true
```
✅ Example 2:
Input:
```
board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output:
false
```

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box (and also in the first column), it is invalid.
---

📌 Constraints
board.length == 9

board[i].length == 9

board[i][j] is a digit 1-9 or '.'.
---

## 💡 Pattern & Approach
The most efficient way to solve this is with a **Single Pass** using **Hash Sets or Arrays**.  
Instead of iterating through the board three separate times (once for rows, once for columns, and once for boxes),  
we check all three conditions **simultaneously** as we traverse the grid.

---

## 🔍 The Logic
We maintain a record of the numbers seen in **each row**, **each column**, and **each 3×3 box**.

**Steps:**

1. **Initialize Data Structures:**
   - `rows[9][9]`: Tracks numbers seen in each row.  
     `rows[i][num] = true` if `num` is present in row `i`.
   - `cols[9][9]`: Tracks numbers seen in each column.  
     `cols[j][num] = true` if `num` is present in column `j`.
   - `boxes[9][9]`: Tracks numbers seen in each 3×3 box.  
     `boxes[k][num] = true` if `num` is present in box `k`.

2. **Single Pass Iteration:**  
   Loop through every cell `(i, j)` in the board.

3. **Check, Validate, and Record:**  
   - If the cell contains a digit:
     - **Get the digit** `d` from `board[i][j]`.
     - **Calculate the Box Index** `k` using:
       ```
       k = (i / 3) * 3 + (j / 3)
       ```
     - **Validate:**
       - If `rows[i][d]` is true → duplicate in row.
       - If `cols[j][d]` is true → duplicate in column.
       - If `boxes[k][d]` is true → duplicate in 3×3 box.
       - If any check is true → return `false`.
     - **Record:**
       - Mark `rows[i][d] = true`
       - Mark `cols[j][d] = true`
       - Mark `boxes[k][d] = true`

4. **Return Result:**  
   If no duplicates are found by the end of iteration → return `true`.

---

## 🏃‍♂️ Dry Run (Spot Check)
**Board Example:**
Let’s trace a couple of cells and see the **box index calculation** in action.

| Cell `(i,j)` | Value | Box Index Calculation                  | k   | Duplicate? | Action                                                                 |
|--------------|-------|----------------------------------------|-----|------------|------------------------------------------------------------------------|
| (4,5)        | '3'   | `(4 / 3) * 3 + (5 / 3) = 1 * 3 + 1`     | 4   | No         | Mark 3 as seen in `rows[4]`, `cols[5]`, `boxes[4]`                     |
| (1,1)        | '6'   | `(1 / 3) * 3 + (1 / 3) = 0 * 3 + 0`     | 0   | No         | Mark 6 as seen in `rows[1]`, `cols[1]`, `boxes[0]`                     |
| (2,2)        | '6'   | `(2 / 3) * 3 + (2 / 3) = 0 * 3 + 0`     | 0   | **Yes**    | Found 6 already in `boxes[0]` → return `false`                         |

---

✅ **Conclusion:**  
By checking **rows, columns, and boxes** in a single traversal, we reduce unnecessary passes and achieve an efficient O(1) space per cell.
---

💻 C++ Code
```
#include <vector>

class Solution {
public:
    bool isValidSudoku(std::vector<std::vector<char>>& board) {
        // Use arrays as hash sets to track seen numbers
        // row[i][digit] is 1 if digit has been seen in row i
        int rows[9][9] = {0}; 
        int cols[9][9] = {0};
        int boxes[9][9] = {0};

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                // Skip empty cells
                if (board[i][j] == '.') {
                    continue;
                }

                // Convert char '1'-'9' to int 0-8
                int digit = board[i][j] - '0' - 1; 

                // Calculate the 3x3 box index (0-8)
                int k = (i / 3) * 3 + (j / 3);

                // Check if the digit has already been seen in the current row, col, or box
                if (rows[i][digit] || cols[j][digit] || boxes[k][digit]) {
                    return false; // Found a duplicate
                }

                // Mark the digit as seen for the current row, col, and box
                rows[i][digit] = 1;
                cols[j][digit] = 1;
                boxes[k][digit] = 1;
            }
        }

        return true; // No duplicates found
    }
};
```
---

📈 Time & Space Complexity
Complexity	Value	Justification
Time	O(1)	We iterate through a 9x9 board, which is a fixed size (81 cells). The number of operations does not change with any "input size N", making it constant time.
Space	O(1)	We use three 9x9 arrays to store the state. Since the size of these arrays is fixed and does not depend on the input, the space complexity is also constant.
---
Export to Sheets
🏷️ Tags
#Array #HashTable #Matrix #LeetCode-Medium
