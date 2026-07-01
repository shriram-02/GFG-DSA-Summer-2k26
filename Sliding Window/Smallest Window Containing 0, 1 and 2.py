class Solution:
    def smallestSubstring(self, s):
        cnt = {'0': 0, '1': 0, '2': 0}
        left = 0
        ans = float('inf')

        for right in range(len(s)):
            if s[right] in cnt:
                cnt[s[right]] += 1

            while cnt['0'] > 0 and cnt['1'] > 0 and cnt['2'] > 0:
                ans = min(ans, right - left + 1)
                if s[left] in cnt:
                    cnt[s[left]] -= 1
                left += 1

        return -1 if ans == float('inf') else ans