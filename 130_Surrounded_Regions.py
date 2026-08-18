class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or board[r][c] == "X":
                return
            
            visited.add((r,c))

            for dr,dc in directions:
                dfs(r+dr, c+dc)

        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows - 1 or j == cols - 1) and board[i][j] == "O" and (i,j) not in visited:
                    dfs(i,j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"