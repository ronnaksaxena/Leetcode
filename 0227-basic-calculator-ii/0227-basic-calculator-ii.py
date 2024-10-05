class Solution:
    def calculate(self, s: str) -> int:
        
        def eval(op, first, second=0):
            if op == '+':
                return first
            elif op == '-':
                return -first
            elif op == '*':
                return first * second
            else:
                # div
                return int(first / second)

        stack = [] # like terms
        cur = 0
        prevOp = '+'
        s = s.strip()
        s += '+'
        for c in s:
            if c == ' ':
                continue
            elif c.isnumeric():
                cur = (cur*10) + int(c)
            else:
                if prevOp in '+-':
                    stack.append(eval(prevOp, cur))
                else:
                    first = stack.pop()
                    stack.append(eval(prevOp, first, cur))

                cur = 0
                prevOp = c

        return sum(stack)

            