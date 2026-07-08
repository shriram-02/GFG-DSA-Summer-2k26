class Solution:
    def cntSubarrays(self, arr, k):
        prefix_sum = 0
        mp = {0: 1}
        ans = 0

        for num in arr:
            prefix_sum += num

            ans += mp.get(prefix_sum - k, 0)
            mp[prefix_sum] = mp.get(prefix_sum, 0) + 1

        return ans