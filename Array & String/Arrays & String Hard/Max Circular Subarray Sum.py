class Solution:
    def maxCircularSum(self, arr):
        # code here
        total_sum = sum(arr)
        
        curr_max = max_sum = arr[0]
        curr_min = min_sum = arr[0]
        
        for x in arr[1:]:
            curr_max = max(x,curr_max + x)
            max_sum = max(max_sum,curr_max)
            
            curr_min = min(x,curr_min + x)
            min_sum = min(min_sum,curr_min)
        if max_sum < 0:
            return max_sum
        return max(max_sum,total_sum - min_sum)