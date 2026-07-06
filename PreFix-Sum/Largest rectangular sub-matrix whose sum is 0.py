from typing import List

class Solution:
    def zeroSumSubmat(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
        
        maxArea = 0
        
        for top in range(n):
            temp = [0] * m
            
            for bottom in range(top, n):
                for j in range(m):
                    temp[j] += mat[bottom][j]
                
                mp = {0: -1}
                curr = 0
                
                for j in range(m):
                    curr += temp[j]
                    
                    if curr in mp:
                        width = j - mp[curr]
                        area = width * (bottom - top + 1)
                        maxArea = max(maxArea, area)
                    else:
                        mp[curr] = j
        
        return maxArea