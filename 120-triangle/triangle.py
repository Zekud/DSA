class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(row,col):
            if row == len(triangle)-1:
                return triangle[row][col]
            if (row,col) in memo:
                return memo[(row,col)]
            memo[(row,col)] = triangle[row][col] + min(dp(row+1,col),dp(row+1,col+1))
            return memo[(row,col)]
    
        return dp(0,0)