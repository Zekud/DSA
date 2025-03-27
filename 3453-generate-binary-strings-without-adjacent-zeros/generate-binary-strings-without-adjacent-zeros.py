class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        arr = ["0","1"]
        def backtrack(path):
            if len(path) == n:
                ans.append("".join(path[:]))
                return 

            for i in range(2):
                if arr[i] == "0" and path and path[-1] == "0":
                    continue
                else:
                    path.append(arr[i])
                    backtrack(path)
                    path.pop()        
        backtrack([])
        return ans