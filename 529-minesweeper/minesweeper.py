class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        
        def count_mines(r, c):
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    count += 1
            return count
        
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != 'E':
                return
            
            mine_count = count_mines(r, c)
            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = 'B'
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        cr, cc = click
        if board[cr][cc] == 'M':
            board[cr][cc] = 'X'
        else:
            dfs(cr, cc)

        return board
