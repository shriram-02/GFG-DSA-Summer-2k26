class Solution:
    def minSteps(self, m, n, d):
        # Code here
        from math import gcd
        
        if d > max(m, n) or d % gcd(m, n) != 0:
            return -1

        def pour(fromJug, toJug, target):
            from_amt = fromJug
            to_amt = 0
            step = 1

            while from_amt != target and to_amt != target:
                temp = min(from_amt, toJug - to_amt)
                to_amt += temp
                from_amt -= temp
                step += 1

                if from_amt == target or to_amt == target:
                    break

                if from_amt == 0:
                    from_amt = fromJug
                    step += 1

                if to_amt == toJug:
                    to_amt = 0
                    step += 1

            return step

        return min(pour(m, n, d), pour(n, m, d))