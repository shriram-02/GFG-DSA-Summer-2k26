class Solution:
    def subarrayXor(self, arr, k):
        xr = 0
        mp = {0: 1}
        ans = 0

        for num in arr:
            xr ^= num

            ans += mp.get(xr ^ k, 0)
            mp[xr] = mp.get(xr, 0) + 1

        return ans