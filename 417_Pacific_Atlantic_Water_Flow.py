class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def bfs(q,visited):

            while q:
                level_size = len(q)
                for _ in range(level_size):
                    row,col = q.popleft()

                    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr,nc = row+dr,col+dc

                        if nr < 0 or nc < 0 or nc >= cols or nr >= rows or heights[row][col] > heights[nr][nc] or (nr,nc) in visited:
                            continue
                        visited.add((nr,nc))
                        q.append((nr,nc))

        rows, cols = len(heights), len(heights[0])

        pacific_visited = set()
        atlantic_visited = set()
        pacific_q = deque()
        atlantic_q = deque()

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    pacific_visited.add((i,j))
                    pacific_q.append((i,j))
                
                if i == rows - 1 or j == cols - 1:
                    atlantic_visited.add((i,j))
                    atlantic_q.append((i,j))

        bfs(pacific_q, pacific_visited)
        bfs(atlantic_q, atlantic_visited)

        res = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific_visited and (i,j) in atlantic_visited:
                    res.append([i,j])
        return res