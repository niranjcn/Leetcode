class Solution:
    def numIslands(self, grid):
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        island = 0
        def dfs(row,col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                return
            grid[row][col] = "0"

            for r,c in directions:
                dfs(row+r,col+c)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island += 1
                    dfs(i,j)
        return island