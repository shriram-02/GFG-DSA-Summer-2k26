from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        # Convert integers to strings
        arr_str = list(map(str, arr))
        
        # Custom comparator: if X + Y > Y + X, X should come before Y
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort using the custom comparator
        arr_str.sort(key=cmp_to_key(compare))
        
        # Join the sorted strings
        result = "".join(arr_str)
        
        # Handle edge case where the array contains only zeros (e.g., [0, 0])
        return "0" if result[0] == "0" else result