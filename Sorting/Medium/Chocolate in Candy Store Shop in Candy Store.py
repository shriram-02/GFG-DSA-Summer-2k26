class Solution:
    def candyStore(self, prices, k):
        prices.sort()
        n = len(prices)
        
        # Find minimum cost (buy cheapest, get expensive free)
        min_cost = 0
        left = 0
        right = n - 1
        while left <= right:
            min_cost += prices[left]
            left += 1
            right -= k
            
        # Find maximum cost (buy expensive, get cheapest free)
        max_cost = 0
        left = 0
        right = n - 1
        while right >= left:
            max_cost += prices[right]
            right -= 1
            left += k
            
        return [min_cost, max_cost]