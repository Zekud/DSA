from collections import defaultdict, deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for emp, mng in enumerate(manager):
            if mng != -1:
                graph[mng].append(emp)

        q = deque([(headID, 0)])  
        max_time = 0

        while q:
            emp, time = q.popleft()
            max_time = max(max_time, time)
            for sub in graph[emp]:
                q.append((sub, time + informTime[emp]))

        return max_time
