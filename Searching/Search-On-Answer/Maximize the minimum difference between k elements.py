class Solution:
    def maxMinDiff(self, arr, k):
        # Code here
        arr.sort()
        
        def is_feasible(mid):
            count = 1
            last_position = arr[0]
            for i in range(1, len(arr)):
                if arr[i] - last_position >= mid:
                    count += 1
                    last_position = arr[i]
                    if count == k:
                        return True
            return False

        low = 0
        high = arr[-1] - arr[0]
        res = 0
        
        while low <= high:
            mid = (low + high) // 2
            if is_feasible(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res