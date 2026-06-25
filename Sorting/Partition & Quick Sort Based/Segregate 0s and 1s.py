class Solution:
    def segregate0and1(self, arr):
        left = 0
        right = len(arr) - 1
        
        while left < right:
            # Increment left index while we see 0 at left
            while arr[left] == 0 and left < right:
                left += 1
                
            # Decrement right index while we see 1 at right
            while arr[right] == 1 and left < right:
                right -= 1
                
            # If left is smaller than right then there is a 1 at left
            # and a 0 at right. Swap them.
            if left < right:
                arr[left] = 0
                arr[right] = 1
                left += 1
                right -= 1