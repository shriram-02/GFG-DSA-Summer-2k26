class Solution:
    def subCount(self, arr, k):
        prefix_sum = 0
        mp = {0: 1}
        ans = 0

        for num in arr:
            prefix_sum += num
            rem = prefix_sum % k

            if rem < 0:
                rem += k

            ans += mp.get(rem, 0)
            mp[rem] = mp.get(rem, 0) + 1

        return ans