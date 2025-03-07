class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = [0]
        for i in range(1,n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return ans

