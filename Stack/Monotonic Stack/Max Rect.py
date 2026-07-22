class Solution:
    def maxArea(self, mat):
        def hist(arr):
            st = []
            res = 0
            arr.append(0)
            for i, h in enumerate(arr):
                while st and arr[st[-1]] > h:
                    ht = arr[st.pop()]
                    w = i if not st else i - st[-1] - 1
                    res = max(res, ht * w)
                st.append(i)
            arr.pop()
            return res

        if not mat:
            return 0

        m = len(mat[0])
        h = [0] * m
        ans = 0

        for row in mat:
            for j in range(m):
                h[j] = h[j] + 1 if row[j] else 0
            ans = max(ans, hist(h))
        return ans