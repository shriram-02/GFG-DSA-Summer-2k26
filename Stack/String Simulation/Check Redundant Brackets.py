class Solution:
    def checkRedundancy(self, s):
        stack = []

        for ch in s:
            if ch == ')':
                has_op = False
                while stack and stack[-1] != '(':
                    if stack[-1] in "+-*/":
                        has_op = True
                    stack.pop()
                stack.pop()
                if not has_op:
                    return 1
            else:
                stack.append(ch)

        return 0