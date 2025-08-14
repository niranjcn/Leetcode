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
```cpp
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

C++

true
✅ Example 2:
Input:

C++

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

C++

false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box (and also in the first column), it is invalid.

📌 Constraints
board.length == 9

board[i].length == 9

board[i][j] is a digit 1-9 or '.'.

💡 Pattern & Approach
The most efficient way to solve this is with a Single Pass using Hash Sets or Arrays. Instead of iterating through the board three times (once for rows, once for columns, once for boxes), we can check all three conditions simultaneously as we traverse the grid.

🔍 The Logic
The core idea is to maintain a record of the numbers seen in each row, each column, and each 3x3 box.

Initialize Data Structures: We'll use three 2D arrays to act as our hash sets:

rows[9][9]: To track numbers seen in each row. rows[i][num] will be true if num is in row i.

cols[9][9]: To track numbers seen in each column. cols[j][num] will be true if num is in column j.

boxes[9][9]: To track numbers seen in each 3x3 box. boxes[k][num] will be true if num is in box k.

Single Pass Iteration: Loop through every cell (i, j) of the board from top-left to bottom-right.

Check, Validate, and Record: For each cell that is not empty (.):

Get the digit d from board[i][j].

Calculate the Box Index (k): This is the clever trick. We map the (i, j) coordinates to a single box index from 0 to 8 using the formula:
$$ k = (\frac{i}{3}) \times 3 + (\frac{j}{3}) $$

Validate: Check if the digit d has already been seen in the current context:

Is d in rows[i]?

Is d in cols[j]?

Is d in boxes[k]?
If the answer to any of these is yes, we have a duplicate. The board is invalid, so we return false immediately.

Record: If the number is valid, we record its presence by setting the corresponding flags to true in our tracking arrays.

Return True: If we complete the entire loop without finding any duplicates, the board is valid.

🏃‍♂️ Dry Run (Spot Check)
Let's trace a few cells to see the logic in action, especially the box index calculation.

Consider board[4][5] = '3':

i = 4, j = 5, digit = 3.

Box Index k = (4 / 3) * 3 + (5 / 3) = 1 * 3 + 1 = 4.

Check: Is 3 in rows[4], cols[5], or boxes[4] yet? Assuming no, we proceed.

Record: Mark 3 as seen in rows[4], cols[5], and boxes[4].

Now, consider an invalid case where board[1][1] = '6' and we later encounter board[2][2] = '6':

For board[1][1] = '6': i=1, j=1, d=6. Box k=0. We mark 6 in rows[1], cols[1], boxes[0].

For board[2][2] = '6': i=2, j=2, d=6. Box k=0.

Check: Is 6 in rows[2]? No. Is 6 in cols[2]? No. Is 6 in boxes[0]? Yes!

A duplicate is found in the same 3x3 box. We immediately return false.

💻 C++ Code
C++

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
📈 Time & Space Complexity
Complexity	Value	Justification
Time	O(1)	We iterate through a 9x9 board, which is a fixed size (81 cells). The number of operations does not change with any "input size N", making it constant time.
Space	O(1)	We use three 9x9 arrays to store the state. Since the size of these arrays is fixed and does not depend on the input, the space complexity is also constant.

Export to Sheets
🏷️ Tags
#Array #HashTable #Matrix #LeetCode-Medium