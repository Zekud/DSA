class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        def inBound(i,j):
            return 0<=i< len(self.matrix) and 0<=j<len(self.matrix[0])
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if inBound(i-1,j):
                    self.matrix[i][j] += self.matrix[i-1][j]
                if inBound(i,j-1):
                    self.matrix[i][j] += self.matrix[i][j-1]
                if inBound(i-1,j-1):
                    self.matrix[i][j] -= self.matrix[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def inBound(i,j):
            return 0<=i< len(self.matrix) and 0<=j<len(self.matrix[0])
        sums = self.matrix[row2][col2]
        if inBound(row1-1,col2):
            sums -= self.matrix[row1-1][col2]
        if inBound(row2,col1-1):
            sums -= self.matrix[row2][col1-1]
        if inBound(row1-1,col1-1):
            sums += self.matrix[row1-1][col1-1]
        return sums

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)