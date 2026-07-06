class Solution:
    def maxRectSum(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
        
        ans = float("-inf")
        
        for left in range(m):
            temp = [0] * n
            
            for right in range(left, m):
                for i in range(n):
                    temp[i] += mat[i][right]
                
                curr = temp[0]
                best = temp[0]
                
                for i in range(1, n):
                    curr = max(temp[i], curr + temp[i])
                    best = max(best, curr)
                
                ans = max(ans, best)
        
        return ans