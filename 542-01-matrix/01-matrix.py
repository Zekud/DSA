class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()

        # Step 1: Add all 0s to the queue and mark 1s as unvisited (-1)
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1  # Unvisited

        # Directions for 4-way movement
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # Step 2: BFS
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # If within bounds and unvisited
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1  # Update distance
                    queue.append((nr, nc))

        return mat
