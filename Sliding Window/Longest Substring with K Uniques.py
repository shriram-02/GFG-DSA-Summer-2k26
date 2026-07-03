class Solution:
    def longestKSubstr(self, s, k):
        left = 0
        freq = {}
        ans = -1

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            if len(freq) == k:
                ans = max(ans, right - left + 1)

        return ans