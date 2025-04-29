class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)

        # reverse edges:
        for a, b in richer:
            graph[b].append(a)

        answer = [-1] * n  #for memo

        def dfs(x):
            if answer[x] != -1:
                return answer[x]

            quietest = x
            for neighbor in graph[x]:
                candidate = dfs(neighbor)
                if quiet[candidate] < quiet[quietest]:
                    quietest = candidate

            answer[x] = quietest
            return quietest

        return [dfs(i) for i in range(n)]