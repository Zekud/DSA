class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for i in range(len(matrix)):
            arr = arr +matrix[i]

        l = 0 
        r = len(arr) - 1
        
        while l <= r:
            mid = (l+r) // 2
            if arr[mid] == target:
                return True
            if arr[mid]> target:
                r= mid-1
            else:
                l = mid + 1
        return False