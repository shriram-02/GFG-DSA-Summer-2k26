class Solution:
    def equalSumSpan(self, a1, a2):
        mp = {}
        diff = 0
        ans = 0

        for i in range(len(a1)):
            diff += a1[i] - a2[i]

            if diff == 0:
                ans = i + 1
            elif diff in mp:
                ans = max(ans, i - mp[diff])
            else:
                mp[diff] = i

        return ans