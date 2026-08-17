class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            area = 1
            for dr,dc in directions:
                area += dfs(r + dr, c + dc)

            return area
            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    res = max(res,dfs(i,j))

        return res