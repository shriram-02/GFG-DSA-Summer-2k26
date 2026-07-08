class Solution:
    def longestSubarray(self, arr, k):
        prefix_sum = 0
        mp = {}
        ans = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == k:
                ans = i + 1

            if (prefix_sum - k) in mp:
                ans = max(ans, i - mp[prefix_sum - k])

            if prefix_sum not in mp:
                mp[prefix_sum] = i

        return ans