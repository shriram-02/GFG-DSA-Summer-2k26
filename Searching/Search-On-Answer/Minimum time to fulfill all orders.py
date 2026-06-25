class Solution:
    def minTime(self, n, arr):
        # Code here
        def donuts_made(time, rank):
            # Solves rank * (x * (x + 1)) // 2 <= time
            low, high = 0, n
            ans = 0
            while low <= high:
                mid = (low + high) // 2
                if rank * (mid * (mid + 1)) // 2 <= time:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        def is_possible(time):
            total_donuts = sum(donuts_made(time, rank) for rank in arr)
            return total_donuts >= n

        low = 1
        high = max(arr) * (n * (n + 1)) // 2
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans