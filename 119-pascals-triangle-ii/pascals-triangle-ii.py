class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] * (rowIndex+1)
        if rowIndex < 2:
            return ans
        prev_row = self.getRow(rowIndex-1)
        for i in range(1,rowIndex):
            ans[i] = prev_row[i] + prev_row[i-1]
        return ans