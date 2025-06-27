class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans =[]
        prev = defaultdict(list)
        for a, b  in prerequisites:
            prev[b].append(a)
        @lru_cache
        def dfs(u,v):
            if u==v:
                return True
            for nr in prev[v]:
                if dfs(u, nr):
                    return True
            return False
                

        for u,v in queries:
            if dfs(u,v):
                ans.append(True)
            else:
                ans.append(False)
        return ans

        