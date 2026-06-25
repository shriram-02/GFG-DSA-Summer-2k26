class Solution:
    def printKClosest(self, arr, k, x):
        # code here
        n = len(arr)
        
        pos = 0
        while pos < n and arr[pos] < x:
            pos += 1
        
        left, right = pos - 1, pos
        res = []
        
        while k:
            if left >= 0 and arr[left] == x:
                left -= 1
                continue
            if right < n and arr[right] == x:
                right += 1
                continue
            
            if left >= 0 and right < n:
                dl = abs(arr[left] - x)
                dr = abs(arr[right] - x)
                
                if dl < dr:
                    res.append(arr[left])
                    left -= 1
                elif dl > dr:
                    res.append(arr[right])
                    right += 1
                else:
                    if arr[left] > arr[right]:
                        res.append(arr[left])
                        left -= 1
                    else:
                        res.append(arr[right])
                        right += 1
            elif left >= 0:
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
            
            k -= 1
        
        return res