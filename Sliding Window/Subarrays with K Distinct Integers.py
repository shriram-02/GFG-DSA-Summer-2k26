class Solution:
    def exactlyK(self, arr, k):
        def atMost(k):
            left = 0
            freq = {}
            ans = 0

            for right in range(len(arr)):
                freq[arr[right]] = freq.get(arr[right], 0) + 1

                while len(freq) > k:
                    freq[arr[left]] -= 1
                    if freq[arr[left]] == 0:
                        del freq[arr[left]]
                    left += 1

                ans += right - left + 1

            return ans

        return atMost(k) - atMost(k - 1)