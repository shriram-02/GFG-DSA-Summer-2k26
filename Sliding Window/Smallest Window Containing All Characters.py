from collections import Counter

class Solution:
    def minWindow(self, s, p):
        if len(p) > len(s):
            return "-1"

        need = Counter(p)
        have = {}
        required = len(need)
        formed = 0

        left = 0
        ans = (float('inf'), 0, 0)

        for right in range(len(s)):
            c = s[right]
            have[c] = have.get(c, 0) + 1

            if c in need and have[c] == need[c]:
                formed += 1

            while formed == required:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                ch = s[left]
                have[ch] -= 1
                if ch in need and have[ch] < need[ch]:
                    formed -= 1
                left += 1

        return "-1" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]