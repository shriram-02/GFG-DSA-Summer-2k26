import bisect

class Solution:
    def kthSmallest(self, mat, k):
        # Code here
        n = len(mat)
        low = mat[0][0]
        high = mat[-1][-1]
        
        while low < high:
            mid = (low + high) // 2
            count = sum(bisect.bisect_right(row, mid) for row in mat)
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low