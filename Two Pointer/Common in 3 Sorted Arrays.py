class Solution:
    def commonElements(self, a, b, c):
        i = j = k = 0
        res = []

        while i < len(a) and j < len(b) and k < len(c):
            if a[i] == b[j] == c[k]:
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
                j += 1
                k += 1
            else:
                m = min(a[i], b[j], c[k])
                if a[i] == m:
                    i += 1
                if b[j] == m:
                    j += 1
                if c[k] == m:
                    k += 1

        return res