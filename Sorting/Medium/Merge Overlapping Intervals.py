class Solution:
    def mergeOverlap(self, arr):
        if not arr:
            return []
            
        # Sort intervals based on their start times
        arr.sort(key=lambda x: x[0])
        
        merged = [arr[0]]
        
        for i in range(1, len(arr)):
            current = arr[i]
            last_merged = merged[-1]
            
            # If current interval overlaps with the last merged interval
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                merged.append(current)
                
        return merged