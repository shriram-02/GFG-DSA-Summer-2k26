class Solution:
    def findPeakGrid(self, mat):
        # code here
        n, m = len(mat), len(mat[0])
        
        left, right = 0, m - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            row = 0
            for i in range(n):
                if mat[i][mid] > mat[row][mid]:
                    row = i
            
            left_val = mat[row][mid - 1] if mid > 0 else -1
            right_val = mat[row][mid + 1] if mid < m - 1 else -1
            
            if mat[row][mid] >= left_val and mat[row][mid] >= right_val:
                return [row, mid]
            elif left_val > mat[row][mid]:
                right = mid - 1
            else:
                left = mid + 1