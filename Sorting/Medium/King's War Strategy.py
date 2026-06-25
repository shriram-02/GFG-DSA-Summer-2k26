import math

class Solution:
    def minSoldiers(self, arr, k):
        n = len(arr)
        needed_lucky = math.ceil(n / 2)
        
        # Calculate cost to make each troop lucky
        costs = []
        for soldiers in arr:
            remainder = soldiers % k
            if remainder == 0:
                costs.append(0)
            else:
                costs.append(k - remainder)
                
        # Sort costs to find the cheapest troops to upgrade
        costs.sort()
        
        # Sum up the lowest costs required to reach the target threshold
        return sum(costs[:needed_lucky])