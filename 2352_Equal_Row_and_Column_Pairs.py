from collections import Counter

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        row_count = Counter(tuple(row) for row in grid)
        result = 0

        for c in range(n):
            column = tuple(grid[r][c] for r in range(n))
            result += row_count[column]

        return result