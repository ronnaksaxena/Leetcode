class Solution:
    def calculate(self, s: str) -> int:
        '''
        case 1: digit
            - update curNumber
        case 2: sign
            - update output = (sign * curNumber)
            - set new sign
            - reset curNumber
        case 3: opening parenthesis
            - push sign onto stack
            - push output onto stack and reset

        case 4: closes parethesis
            - update output = stack.pop() (sign) * output + stack.pop() (prevResult)


        end return output * sign

        "(1+(4+5+2)-3)+(6+8)"
                     i
        s = [0, +, ]
        sign = -1
        output = 11
        curNumber = 3
        '''

        stack = []
        sign = 1
        output = 0 # sum for current level exploring
        curNumber = 0

        for c in s:
            # Updating digit
            if c.isdigit():
                curNumber = curNumber*10 + int(c)
            # add parsed num to level sum
            elif c in '+-':
                output += (sign * curNumber)
                sign = 1 if c == '+' else -1
                curNumber = 0
            # Store outer level sum in stack and sign of next level
            elif c == '(':
                stack.append(output)
                stack.append(sign)
                sign = 1
                output = 0
            # Eval current level, negate if minus, sum with outer level
            elif c == ')':
                output += (curNumber * sign)
                output *= stack.pop() # set sign
                output += stack.pop() # add outer computation
                curNumber = 0

        # Add last parsed number to global sum
        return output + (sign*curNumber)

        