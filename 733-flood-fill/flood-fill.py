class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque([(sr,sc)])

        dir =[(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(r,c):
            return 0<=r<len(image) and 0<=c<len(image[0])
        
        target = image[sr][sc]
        if target == color:
            return image
        visited = set()
        while queue:
            r,c = queue.popleft()
            visited.add((r,c))
            if image[r][c] ==target:
                image[r][c] =color
            for dr,dc in dir:
                nr =r + dr
                nc = c+ dc
                if inbound(nr,nc) and image[nr][nc] ==target and (nr,nc) not in visited:
                    queue.append((nr,nc))
        return image



           
            



         