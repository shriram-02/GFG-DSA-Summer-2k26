class Solution:
    def nQueen(self, n):
        ans = []
        col = set()
        diag1 = set()
        diag2 = set()
        board = []

        def backtrack(r):
            if r == n:
                ans.append(board[:])
                return

            for c in range(n):
                if c in col or (r - c) in diag1 or (r + c) in diag2:
                    continue

                col.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                board.append(c + 1)

                backtrack(r + 1)

                board.pop()
                col.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return ans