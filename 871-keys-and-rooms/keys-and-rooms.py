class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        graph = defaultdict(list)
        for i , arr in enumerate(rooms):
            for num in arr:
                graph[i].append(num)
        
        visited = [False] * n
        def dfs(node):
            if visited[node]:
                return 
            visited[node] = True
            for neigh in graph[node]:
                if not visited[neigh]:
                    dfs(neigh)
        dfs(0)
        for i in range(n):
            if not visited[i]:
                return False
        return True