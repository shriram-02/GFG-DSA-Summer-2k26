import math

class Solution:
    def bananas(self, arr, k):
        # Code here
        low = 1
        high = max(arr)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            hours = sum(math.ceil(pile / mid) for pile in arr)
            if hours <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans