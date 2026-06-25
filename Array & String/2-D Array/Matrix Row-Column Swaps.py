class Solution:
    def solveQueries(self, m, n, queries):
        # code here
        rows = list(range(m))
        cols = list(range(n))
        ans = []

        for typ, a, b in queries:
            if typ == 1:
                rows[a], rows[b] = rows[b], rows[a]

            elif typ == 2:
                cols[a], cols[b] = cols[b], cols[a]

            else:
                value = rows[a] * n + cols[b] + 1
                ans.append(value)

        return ans