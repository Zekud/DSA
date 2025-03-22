class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def listPermute(path, check):
            if len(path) == len(nums):
                result.append(path[:])
                return 

            for c in check:
                if c not in path:
                    path.append(c)
                    listPermute(path,check)
                    path.pop()
        listPermute([],set(nums))

        return result
