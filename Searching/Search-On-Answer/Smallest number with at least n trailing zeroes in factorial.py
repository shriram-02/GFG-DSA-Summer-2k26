class Solution:
    def findNum(self, n):
        # Code here
        def check(p, n):
            count = 0
            factor = 5
            while factor <= p:
                count += p // factor
                factor *= 5
            return count >= n

        if n == 1:
            return 5
            
        low = 0
        high = 5 * n
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid, n):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans