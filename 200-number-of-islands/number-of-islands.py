class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = [[False] * cols for i in range(rows)]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        def inbound(r,c):
            return 0 <= r < rows and 0 <= c < cols
        def dfs(r,c):
            if not inbound(r,c):
                return 
            if grid[r][c] == "0" or visited[r][c]:
                return 
            visited[r][c] = True
            for dr,dc in dirs:
                dfs(r+dr,c+dc)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i,j)
                    count+=1
        return count
