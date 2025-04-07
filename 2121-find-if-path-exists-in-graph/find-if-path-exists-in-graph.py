class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjlist = defaultdict(list)
        for x,y in edges:
            adjlist[x].append(y)
            adjlist[y].append(x)
        visited = set()
        def recur(node):
            nonlocal destination
            if node == destination:
                return True
            visited.add(node)
            for n in adjlist[node]:
                if n not in visited:
                    found = recur(n)
                    if found:
                        return True
            return False
        return recur(source)