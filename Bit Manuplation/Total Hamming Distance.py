class Solution:
    def totHammingDist(self, arr):
        # code here
        n = len(arr)
        ans = 0

        for i in range(32):
            cnt = 0
            for x in arr:
                if x & (1 << i):
                    cnt += 1
            ans += cnt * (n - cnt)

        return ans