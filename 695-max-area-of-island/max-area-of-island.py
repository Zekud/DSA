class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = [[False] * cols for i in range(rows)]
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        area = 0
        def inbound(r,c):
            return 0 <= r < rows and 0 <= c < cols
        def dfs(r,c):
            if not inbound(r,c):
                return 0
            if grid[r][c] == 0 or visited[r][c]:
                return 0
            visited[r][c] = True
            count = 1
            for dr,dc in dirs:
                count += dfs(r+dr,c+dc)
            return count
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    count = dfs(i,j)
                    area = max(area,count)
        return area