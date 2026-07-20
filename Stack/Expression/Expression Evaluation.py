class Solution:
    def evaluateInfix(self, arr):
        def precedence(op):
            if op in '+-':
                return 1
            if op in '*/':
                return 2
            return 0

        def apply(a, b, op):
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
            return int(a / b)

        values = []
        ops = []

        for token in arr:
            if token == '(':
                ops.append(token)
            elif token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                values.append(int(token))
            elif token == ')':
                while ops[-1] != '(':
                    b = values.pop()
                    a = values.pop()
                    values.append(apply(a, b, ops.pop()))
                ops.pop()
            else:
                while ops and ops[-1] != '(' and precedence(ops[-1]) >= precedence(token):
                    b = values.pop()
                    a = values.pop()
                    values.append(apply(a, b, ops.pop()))
                ops.append(token)

        while ops:
            b = values.pop()
            a = values.pop()
            values.append(apply(a, b, ops.pop()))

        return values[-1]