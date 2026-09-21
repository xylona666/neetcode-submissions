class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i= 0
        m = len(matrix)
        n = len(matrix[0])
        j = m*n-1
        while i <= j:
            mid = (i+j)//2
            row = mid//n
            col = mid%n
            if target == matrix[row][col]:
                return True
            elif matrix[row][col] < target:
                i = mid+1
            elif matrix[row][col] > target:
                j = mid-1
        return False