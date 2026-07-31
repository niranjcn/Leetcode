class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        fresh = 0
        minutes = 0
        q = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        while q and fresh > 0:
            for _ in range(len(q)):
                row,col = q.popleft()
                for r,c in directions:
                    if row + r < 0 or row + r >= rows or col + c < 0 or col + c >= cols or grid[row+r][col+c] != 1:
                        continue
                    elif grid[row + r][col + c] == 1:
                        grid[row + r][col + c] = 2
                        q.append((row + r,col + c))
                        fresh -= 1
            minutes += 1
        return minutes if fresh == 0 else -1