class Solution:
    def visibleBuildings(self, arr):
        cnt = 0
        mx = 0
        for h in arr:
            if h >= mx:
                cnt += 1
                mx = h
        return cnt