class Solution:
    def calculate(self, s: str) -> int:
        '''
        evalute when you reach an operator or )
        input: string, output: int

        - truncate down on /
        - valid input, numeric with operators


        - evaluate in order of operations, (), */, +-
        - stack to store terms that sum up to answer

        stack = [1, answer]

        - if encoutner opening parenthesis push operator p
        - ((1+1))
        [2]
        - if encounter ) while top of stack != p:
            pop and aggregate a sum of that term in the parenthesis

        s = "2*(5+5*2)/3+(6/2+8)" <- '+'
                     i
        stack = [2, 'p', 5, 10]
        cur = 2
        prevOperator = *

    1. digit update cur
    2. opening parenthesis, push p onto stack, evaluate current term + push onto stack
        prevOperator = +
    3. # closing parenthese or new operatore
        evalue previous term + push onto stack
        while top of stack != p
            temp += stack.top

        push temp onto stack
    4. sum all terms i stack

    Time: O(N) for our stack
    Space: O(N) for stack
        '''

        def evaluate(operand, first, second=0):
            if operand == '+':
                return first
            if operand == '-':
                return -first
            if operand == '*':
                return first*second
            else:
                # integer division
                return int(first/second)
        
        cur, stack, prevOperand = 0, [], '+'
        s += '+'

        for c in s:
            if c.isnumeric():
                cur = cur*10 + int(c)
            elif c == '(': # FIXME
                stack.append(prevOperand)
                prevOperand = '+'
            else:
                # closing parenthesis or new operand
                if prevOperand in '+-':
                    stack.append(evaluate(prevOperand, cur))
                elif prevOperand in '*/':
                    first = stack.pop()
                    stack.append(evaluate(prevOperand, first, cur))
                cur = 0
                prevOperand = c
                # Is this a closing parenthesis?
                if c == ')':
                    tempTerm = 0
                    while type(stack[-1]) == int:
                        tempTerm += stack.pop()
                    cur = tempTerm
                    prevOperand = stack.pop()

        return sum(stack)



        