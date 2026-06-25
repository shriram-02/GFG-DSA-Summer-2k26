class Solution:
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        res = []
        i, j = 0, 0
        n, m = len(a), len(b)
        
        while i < n or j < m:
            # Pick the smaller element among the current positions
            if i < n and (j >= m or a[i] <= b[j]):
                curr = a[i]
                i += 1
            else:
                curr = b[j]
                j += 1
                
            # Insert to result if it's the first element or different from previous
            if not res or res[-1] != curr:
                res.append(curr)
                
        return res