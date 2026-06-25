class Solution:
    def minCost(self, heights, cost):
        # Code here
        def compute_cost(target_height):
            return sum(abs(h - target_height) * c for h, c in zip(heights, cost))

        low = min(heights)
        high = max(heights)
        ans = compute_cost(low)
        
        while low <= high:
            mid = (low + high) // 2
            cost_mid = compute_cost(mid)
            cost_mid_plus = compute_cost(mid + 1)
            
            ans = min(ans, cost_mid)
            if cost_mid < cost_mid_plus:
                high = mid - 1
            else:
                low = mid + 1
                
        return ans