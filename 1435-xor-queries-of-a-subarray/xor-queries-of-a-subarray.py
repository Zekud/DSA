class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = []
        x = 0
        pre.append(x)
        for num in arr:
            x^=num
            pre.append(x)
        ans = []
        for i,j in queries:
            ans.append(pre[j+1]^pre[i])
        return ans