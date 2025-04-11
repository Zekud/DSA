class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        visited = [[False] * cols for i in range(rows)]
        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        def inbound(r,c):
            return 0<=r<rows and 0 <=c<cols
        def dfs(r,c):
            if not inbound(r,c) or grid[r][c] == 0:
                return 1
            if visited[r][c]:
                return 0

            visited[r][c] = True
            peri = 0
            for row,col in dir:
                peri += dfs(r+row,c+col)
            return peri
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i,j)
