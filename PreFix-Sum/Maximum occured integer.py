class Solution:
    def maxOccured(self, L, R):
        mx = max(R)
        diff = [0] * (mx + 2)

        for l, r in zip(L, R):
            diff[l] += 1
            diff[r + 1] -= 1

        ans = 0
        cur = 0
        best = -1

        for i in range(mx + 1):
            cur += diff[i]
            if cur > best:
                best = cur
                ans = i

        return ans