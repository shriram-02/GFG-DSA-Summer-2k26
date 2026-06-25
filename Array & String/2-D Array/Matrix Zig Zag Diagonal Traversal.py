class Solution:
    def matrixDiagonally(self, mat):
        # code here
        n = len(mat)
        ans = []

        for d in range(2 * n - 1):
            temp = []

            row = 0 if d < n else d - n + 1
            col = d if d < n else n - 1

            while row < n and col >= 0:
                temp.append(mat[row][col])
                row += 1
                col -= 1

            if d % 2 == 0:
                temp.reverse()

            ans.extend(temp)

        return ans