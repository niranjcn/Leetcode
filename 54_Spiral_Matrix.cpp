class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();
        int top = 0, bottom = row - 1, left = 0, right = col - 1;
        vector<int> result;

        while (top <= bottom && left <= right) {
            // traverse top row
            for (int j = left; j <= right; j++) {
                result.push_back(matrix[top][j]);
            }
            top++;

            // traverse right column
            for (int i = top; i <= bottom; i++) {
                result.push_back(matrix[i][right]);
            }
            right--;

            // traverse bottom row
            if (top <= bottom) {
                for (int j = right; j >= left; j--) {
                    result.push_back(matrix[bottom][j]);
                }
                bottom--;
            }

            // traverse left column
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
