class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int row[9][9] = {0};
        int col[9][9] = {0};
        int grid[9][9] = {0};
        for(int i = 0;i<board.size();i++){
            for(int j = 0;j<board[0].size();j++){
                if(board[i][j] != '.'){
                    int ch = board[i][j] - '0' - 1;
                    int k = i / 3 * 3 + j / 3;
                    if(row[i][ch] || col[j][ch] || grid[k][ch]){
                        return false;
                    }
                    row[i][ch] = 1;
                    col[j][ch] = 1;
                    grid[k][ch] = 1;

                }
            }
        }
        return true;
    }
};