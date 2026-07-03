from collections import Counter

class Solution:
    def search(self, pat, txt):
        k = len(pat)
        if k > len(txt):
            return 0

        need = Counter(pat)
        window = Counter()
        ans = 0

        for i in range(len(txt)):
            window[txt[i]] += 1

            if i >= k:
                window[txt[i - k]] -= 1
                if window[txt[i - k]] == 0:
                    del window[txt[i - k]]

            if window == need:
                ans += 1

        return ans