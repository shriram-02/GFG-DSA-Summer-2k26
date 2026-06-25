class Solution:
    def getSecondLargest(self, arr):
        # code here
        first = second = -1
        
        for x in arr:
            if x > first:
                second = first
                first = x
            elif first > x > second:
                second = x
                
        return second