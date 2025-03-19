class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        ans = []
        def backtrack(first_num):
            if len(path) == k:
                ans.append(path[:])
                return
            for num in range(first_num,n+1):
                path.append(num)
                backtrack(num+1)
                path.pop()
        backtrack(1)
        return ans