class Solution:
    def countSubarrays(self, arr, k):
        freq = {0: 1}
        odd = 0
        ans = 0

        for x in arr:
            if x % 2:
                odd += 1
            ans += freq.get(odd - k, 0)
            freq[odd] = freq.get(odd, 0) + 1

        return ans