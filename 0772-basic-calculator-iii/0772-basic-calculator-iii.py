class Solution:
    def calculate(self, s: str) -> int:
        '''
        Qs:
        - input: string, output: int (evaluation)
        - valid s, nonempty
        - '+', '-', '*', '/' , (),
            - / to truncate towards 0 int(dividend/ divisor)
            - no divide by 0
        - valid answer to each expression

        Idea: store like terms in a stack that can be summed to create final answer

        2 + 2 * 5 <- +
                       
        s = [2, 10] sum(stack) => 12
        prevOperation = *
        push onto stack whenever we encounter an operation


        2*(5+5*2)/3+(6/2+8) <- +
                    i
        s = [10]
        set cur to evaluation of term
        prevOperand = stack.pop() => *

        When reach ) evaluate all terms up until operand and then evaluate parenthesis with initial operate retrieved from the stack

        Algo:
            -def helperEvaluate(operation, arg, arg2)
            - init stack, cur int, prevOperand string
            - iterate through the input and push terms onto stack
            - return sum(stack)

        Time: O(N * number of parethesis pairs)
        Space: O(N) for stack


        '''

        def evaluate(operation, x, y=0):
            if operation == '+':
                return x
            elif operation == '-':
                return -x
            elif operation == '*':
                return x*y
            else:
                # truncate to 0
                return int(x/y)
        
        stack = []
        curNumber = 0
        prevOperand = '+'

        s += '+'

        for c in s:
            # print(c, stack, curNumber, prevOperand)
            if c.isdigit():
                curNumber = (curNumber*10) + int(c)
            elif c == '(':
                stack.append(prevOperand)
                prevOperand = '+'
            else:
                # operation
                if prevOperand in '+-':
                    stack.append(evaluate(prevOperand, curNumber))
                    curNumber = 0
                    prevOperand = c
                # closing parenthesis
                elif prevOperand in '*/':
                    firstArg = stack.pop()
                    stack.append(evaluate(prevOperand, firstArg, curNumber))
                    curNumber = 0
                    prevOperand = c
                if c == ')':
                    while stack and type(stack[-1]) == int:
                        curNumber += stack.pop()
                    
                    prevOperand = stack.pop()

        return sum(stack)


        