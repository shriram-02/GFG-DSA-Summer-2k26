import bisect

class Solution:
    def median(self, mat):
        # Code here
        r, c = len(mat), len(mat[0])
        low = min(mat[i][0] for i in range(r))
        high = max(mat[i][-1] for i in range(r))
        desired = (r * c + 1) // 2
        
        while low < high:
            mid = (low + high) // 2
            count = sum(bisect.bisect_right(row, mid) for row in mat)
            if count < desired:
                low = mid + 1
            else:
                high = mid
        return low