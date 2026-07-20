class Solution:
    def infixToPostfix(self, s):
        prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        stack = []
        ans = []

        for ch in s:
            if ch.isalnum():
                ans.append(ch)
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                while stack and stack[-1] != '(':
                    ans.append(stack.pop())
                stack.pop()
            else:
                while (stack and stack[-1] != '(' and
                       (prec[stack[-1]] > prec[ch] or
                        (prec[stack[-1]] == prec[ch] and ch != '^'))):
                    ans.append(stack.pop())
                stack.append(ch)

        while stack:
            ans.append(stack.pop())

        return "".join(ans)