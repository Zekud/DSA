class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n= len(graph)
        rgraph = defaultdict(list)
        outdegree = [0] * n
        for i in range(n):
            for num in graph[i]:
                rgraph[num].append(i)
            outdegree[i] = len(graph[i])
        queue = deque([i for i in range(len(graph)) if outdegree[i] == 0])
        safe = [False] * n
        while queue:
            node = queue.popleft()
            safe[node] = True
            for neigh in rgraph[node]:
                outdegree[neigh] -=1
                if outdegree[neigh] == 0:
                    queue.append(neigh)
        return [i for i in range(n) if safe[i]]

        