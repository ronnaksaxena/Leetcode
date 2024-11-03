class Solution:
    def calculate(self, s: str) -> int:
        '''
        "(1+(4+5+2)-3)+(6+8)"
                  i
        s = [0, +, ]
        res = 12
        curNumber = 4
        sign = -1

        EDGE CASE: ignore whitespace
        case 1: num
            - update curNumber
        case 2: sign
            - update/reset output
            - update/reset sign
        case 3: open parenthesis
            - store computation & sign so far in stack
            - reset curNumber, sign, otutput
        case 4: close parenthesis => compute this level + outer level
            - this level result = result + stack.pop() {sign}
            - outer level + current level
            output = output.pop() + current level
        case 5: reached end of string
            - final result is rest + (sign + curNumber)

        Time: O(n)
        Space: O(n) for stack

        '''

        stack = []
        curNumber, result = 0, 0
        sign = 1

        for c in s:
            if c == ' ':
                continue
            # print(result, curNumber, stack, sign)
            if c.isdigit():
                curNumber = curNumber*10 + int(c)
            elif c in "+-":
                result += (curNumber * sign)
                sign = 1 if c == '+' else -1
                curNumber = 0
            elif c == '(':
                stack.append(result)
                result = 0
                stack.append(sign)
                sign = 1
            elif c == ')':
                # (4 + 5)
                # curNumber = 0
                # res = 9
                # sign = 1
                # stack [3, +]
                result += (sign * curNumber)
                curNumber = 0
                # update negation of level result
                result *= stack.pop()
                # sum with outer level result
                result = stack.pop() + result
                sign = 1
        
        # Add final computation to end of string
        return result + (sign * curNumber)

        