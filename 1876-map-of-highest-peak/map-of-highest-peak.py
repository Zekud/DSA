class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        height = [[-1] * cols for _ in range(rows)]
        queue = deque()

        # Step 1: Initialize water cells
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    height[r][c] = 0
                    queue.append((r, c))

        # Step 2: BFS from water
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    queue.append((nr, nc))

        return height
