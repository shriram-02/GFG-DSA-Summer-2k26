class Solution:
    def maxSum(self, arr):
        n = len(arr)
        total_sum = sum(arr)
        
        # Initial configuration calculation (R_0)
        curr_sum = sum(i * val for i, val in enumerate(arr))
        max_sum = curr_sum
        
        # Rolling transitions using derivation: R_j = R_{j-1} + total_sum - n * arr[n-j]
        for j in range(1, n):
            curr_sum = curr_sum + total_sum - n * arr[n - j]
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        return max_sum