class Solution:
    # Function to return a list containing the intersection of two sorted arrays.
    def Intersection(self, a, b):
        res = []
        i, j = 0, 0
        n, m = len(a), len(b)
        
        while i < n and j < m:
            if a[i] < b[j]:
                i += 1
            elif b[j] < a[i]:
                j += 1
            else:
                # Elements match, insert if it is a unique match
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
                j += 1
                
        return res