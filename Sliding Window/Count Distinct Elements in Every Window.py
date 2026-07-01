from collections import defaultdict

class Solution:
    def countDistinct(self, arr, k):
        freq = defaultdict(int)
        ans = []

        for i in range(k):
            freq[arr[i]] += 1
        ans.append(len(freq))

        for i in range(k, len(arr)):
            freq[arr[i - k]] -= 1
            if freq[arr[i - k]] == 0:
                del freq[arr[i - k]]

            freq[arr[i]] += 1
            ans.append(len(freq))

        return ans