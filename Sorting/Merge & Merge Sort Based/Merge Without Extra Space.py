import math

class Solution:
    # Function to merge the arrays using the Gap Method (Shell Sort variant)
    def mergeArrays(self, a, b):
        n, m = len(a), len(b)
        gap = math.ceil((n + m) / 2)
        
        while gap > 0:
            i = 0
            j = gap
            
            while j < (n + m):
                # Case 1: Both pointers are in array 'a'
                if j < n:
                    if a[i] > a[j]:
                        a[i], a[j] = a[j], a[i]
                # Case 2: One pointer is in 'a' and one is in 'b'
                elif i < n and j >= n:
                    if a[i] > b[j - n]:
                        a[i], b[j - n] = b[j - n], a[i]
                # Case 3: Both pointers are in array 'b'
                else:
                    if b[i - n] > b[j - n]:
                        b[i - n], b[j - n] = b[j - n], b[i - n]
                i += 1
                j += 1
                
            if gap == 1:
                break
            gap = math.ceil(gap / 2)