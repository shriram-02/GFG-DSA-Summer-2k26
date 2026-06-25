class Solution:
    def countXInRange(self, arr, queries):
        # code here
        from bisect import bisect_left, bisect_right
        
        ans = []
        
        for l, r, x in queries:
            left = bisect_left(arr, x, l, r + 1)
            right = bisect_right(arr, x, l, r + 1)
            ans.append(right - left)
        
        return ans