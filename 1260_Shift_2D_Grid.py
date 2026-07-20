class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        target = m * n
        k %= target

        matrix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):

                old_index = (i * n) + j
                new_index = (old_index + k) % target

                row = new_index // n
                col = new_index % n

                matrix[row][col] = grid[i][j]
        return matrix