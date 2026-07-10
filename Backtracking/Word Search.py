class Solution:
    def isWordExist(self, mat, word):
        n, m = len(mat), len(mat[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or j < 0 or i >= n or j >= m or mat[i][j] != word[k]:
                return False

            temp = mat[i][j]
            mat[i][j] = '#'

            found = (
                dfs(i + 1, j, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j + 1, k + 1) or
                dfs(i, j - 1, k + 1)
            )

            mat[i][j] = temp
            return found

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False