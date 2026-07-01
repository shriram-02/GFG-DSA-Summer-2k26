class Solution:
    def minWindow(self, s1, s2):
        n, m = len(s1), len(s2)
        start = -1
        min_len = float('inf')

        i = 0
        while i < n:
            if s1[i] == s2[0]:
                j = i
                k = 0

                while j < n and k < m:
                    if s1[j] == s2[k]:
                        k += 1
                    j += 1

                if k == m:
                    end = j - 1
                    k = m - 1
                    j = end

                    while k >= 0:
                        if s1[j] == s2[k]:
                            k -= 1
                        j -= 1

                    j += 1
                    if end - j + 1 < min_len:
                        min_len = end - j + 1
                        start = j

                    i = j
            i += 1

        return "" if start == -1 else s1[start:start + min_len]