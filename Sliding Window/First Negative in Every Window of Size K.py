from collections import deque

class Solution:
    def firstNegInt(self, arr, k):
        q = deque()
        ans = []

        for i in range(len(arr)):
            if arr[i] < 0:
                q.append(i)

            if i >= k - 1:
                while q and q[0] <= i - k:
                    q.popleft()

                ans.append(arr[q[0]] if q else 0)

        return ans