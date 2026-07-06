class Solution:
    def findMean(self, arr, queries):
        # code here
        pref = [0]
        
        for num in arr:
            pref.append(pref[-1] + num)
        
        ans = []
        
        for l, r in queries:
            total = pref[r + 1] - pref[l]
            ans.append(total // (r - l + 1))
        
        return ans