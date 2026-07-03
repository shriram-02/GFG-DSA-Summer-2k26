class Solution:
    def countSubstr(self, s, k):
        def atMost(k):
            if k < 0:
                return 0

            left = 0
            freq = {}
            ans = 0

            for right in range(len(s)):
                freq[s[right]] = freq.get(s[right], 0) + 1

                while len(freq) > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1

                ans += right - left + 1

            return ans

        return atMost(k) - atMost(k - 1)