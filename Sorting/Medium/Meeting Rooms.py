class Solution:
    def canAttend(self, arr):
        # Sort meetings by their start times
        arr.sort(key=lambda x: x[0])
        
        for i in range(1, len(arr)):
            # If the current meeting starts before the previous one ends
            if arr[i][0] < arr[i-1][1]:
                return False
                
        return True