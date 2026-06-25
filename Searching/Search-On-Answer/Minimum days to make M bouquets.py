class Solution:
    def minDaysToMake(self, arr, m, k):
        # Code here
        if m * k > len(arr):
            return -1
            
        def get_bouquets(days):
            bouquets = 0
            flowers = 0
            for bloom in arr:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets

        low = min(arr)
        high = max(arr)
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if get_bouquets(mid) >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans