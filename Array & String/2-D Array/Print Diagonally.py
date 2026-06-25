class Solution:
    def diagView(self, mat):
        # code here
        n = len(mat)
        ans = []

        for d in range(2 * n - 1):
            for i in range(n):
                j = d - i
                if 0 <= j < n:
                    ans.append(mat[i][j])

        return ans