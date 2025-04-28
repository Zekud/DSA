class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(v):
            if v in visited:
                return graph[v]
            visited.add(v)
            val = []
            for u in graph[v]:
                val += dfs(u)
            graph[v] = sorted(set(val+graph[v]))
            return graph[v]

        result = []
        visited = set()
        graph = defaultdict(list)
        for x,y in edges:
            graph[y].append(x)
        for i in range(n):
            if i not in visited:
                dfs(i)
        for i in range(n): result.append(graph[i])
        return result
        