class Solution:
    def evaluatePostfix(self, arr):
        stack = []

        for token in arr:
            if token in "+-*/^":
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
                else:
                    stack.append(a ** b)
            else:
                stack.append(int(token))

        return stack[-1]