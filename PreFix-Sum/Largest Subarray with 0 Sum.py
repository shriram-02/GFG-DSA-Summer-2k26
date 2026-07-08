class Solution:
    def maxLen(self, arr):
        prefix_sum = 0
        mp = {}
        ans = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == 0:
                ans = i + 1

            if prefix_sum in mp:
                ans = max(ans, i - mp[prefix_sum])
            else:
                mp[prefix_sum] = i

        return ans