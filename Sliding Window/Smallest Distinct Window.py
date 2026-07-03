from collections import Counter

class Solution:
    def findSubString(self, s):
        required = len(set(s))
        freq = {}
        left = 0
        formed = 0
        ans = len(s)

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            if freq[s[right]] == 1:
                formed += 1

            while formed == required:
                ans = min(ans, right - left + 1)
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                    formed -= 1
                left += 1

        return ans