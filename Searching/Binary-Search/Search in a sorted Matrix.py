class Solution:
    def searchMatrix(self, mat, x):
        # code here
        n, m = len(mat), len(mat[0])
        
        low, high = 0, n * m - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            val = mat[mid // m][mid % m]
            
            if val == x:
                return True
            elif val < x:
                low = mid + 1
            else:
                high = mid - 1
                
        return False