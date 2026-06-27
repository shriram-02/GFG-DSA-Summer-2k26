class Solution:
    def isValid(self, mat):
        # code here
        # Check rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if mat[i][j] != 0:
                    if mat[i][j] in seen:
                        return False
                    seen.add(mat[i][j])

        # Check columns
        for j in range(9):
            seen = set()
            for i in range(9):
                if mat[i][j] != 0:
                    if mat[i][j] in seen:
                        return False
                    seen.add(mat[i][j])

        # Check 3x3 subgrids
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                seen = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if mat[i][j] != 0:
                            if mat[i][j] in seen:
                                return False
                            seen.add(mat[i][j])

        return True