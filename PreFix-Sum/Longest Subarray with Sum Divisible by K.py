class Solution:
    def longestSubarrayDivK(self, arr, k):
        prefix_sum = 0
        mp = {0: -1}
        ans = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]
            rem = prefix_sum % k

            if rem < 0:
                rem += k

            if rem in mp:
                ans = max(ans, i - mp[rem])
            else:
                mp[rem] = i

        return ans