class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        min_heap = [(0,k)]
        visited = {}
        while min_heap:
            time,node = heappop(min_heap)
            if node in visited:
                continue
            visited[node] = time
            for nei,wt in graph[node]:
                # if nei not in visited:
                    heappush(min_heap,(time + wt,nei))
        if len(visited) == n:
            return max(visited.values())
        return -1