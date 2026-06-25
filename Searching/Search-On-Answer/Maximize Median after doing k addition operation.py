class Solution:
    def maximizeMedian(self, arr, k):
        # code here
        arr.sort()
        n = len(arr)

        def possible(x):
            ops = 0

            if n % 2:
                for i in range(n // 2, n):
                    if arr[i] < x:
                        ops += x - arr[i]
            else:
                m1 = n // 2 - 1
                m2 = n // 2

                if arr[m1] < x:
                    ops += x - arr[m1]

                if arr[m2] < x:
                    ops += x - arr[m2]

            return ops <= k

        if n % 2:
            low = arr[n // 2]
        else:
            low = (arr[n // 2 - 1] + arr[n // 2]) // 2

        high = low + k + max(arr)
        ans = low

        while low <= high:
            mid = (low + high) // 2

            if possible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans