class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        diagonals = [(-1,0),(0,-1),(1,0),(0,1)]
        visited = set()
        def inBound(x,y): return 0<=x<len(board) and 0<=y<len(board[0])
        def dfs(x,y):
            if not inBound(x,y) or (x,y) in visited or board[x][y] == 'X':
                return
            
            visited.add((x,y))
            for i,j in diagonals:
                nx,ny = i+x, j+y
                dfs(nx,ny)

        for i in range(len(board)):
            dfs(i,0)
            dfs(i,len(board[0])-1)

        for j in range(1,len(board[0])):
            dfs(0,j)
            dfs(len(board)-1,j)

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited:
                    board[i][j] = 'X'

        