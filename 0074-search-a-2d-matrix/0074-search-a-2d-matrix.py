class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L,R = 0,len(matrix)-1
        while L <= R:
            mid1 = (L+R)//2
            l,r = 0,len(matrix[0])-1
            while l<=r:
                mid2 = (l+r)//2
                if target > matrix[mid1][mid2]:
                    l = mid2 + 1
                elif target < matrix[mid1][mid2]:
                    r = mid2-1
                else:
                    return True
            if target > matrix[mid1][r]:
                L = mid1 + 1
            elif target < matrix[mid1][r]:
                R = mid1-1
            else:
                return True
        return False
                    