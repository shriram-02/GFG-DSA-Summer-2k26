class Solution:
    def medianOf2(self, a, b):
        #code here

        if len(a) > len(b):
            a, b = b, a

        n = len(a)

        low, high = 0, n

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = n - cut1

            l1 = float('-inf') if cut1 == 0 else a[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else b[cut2 - 1]

            r1 = float('inf') if cut1 == n else a[cut1]
            r2 = float('inf') if cut2 == n else b[cut2]

            if l1 <= r2 and l2 <= r1:
                return (max(l1, l2) + min(r1, r2)) / 2

            elif l1 > r2:
                high = cut1 - 1

            else:
                low = cut1 + 1