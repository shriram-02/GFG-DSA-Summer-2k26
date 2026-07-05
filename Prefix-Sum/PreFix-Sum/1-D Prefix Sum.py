class Solution:
    def prefSum(self, arr):
        # code here
        prefix = []
        curr = 0
        
        for num in arr:
            curr += num
            prefix.append(curr)
            
        return prefix