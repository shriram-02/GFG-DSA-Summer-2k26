class Solution:
    def checkRedundancy(self, s):
        stack = []

        for ch in s:
            if ch == ')':
                hasOp = False
                while stack[-1] != '(':
                    if stack[-1] in "+-*/":
                        hasOp = True
                    stack.pop()
                stack.pop()
                if not hasOp:
                    return 1
            else:
                stack.append(ch)

        return 0