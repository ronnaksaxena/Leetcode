class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        - input: List[str]
        - ouptut: int
        - operands & +- ints
        - no divide by zero
        
        ["4","13","5","/","+"]
                           i
                           -
                         10 - 5 => 5
        stack = [10, 5]
        
        (4 + (13 // 5))
        
        Idea: Stack
            - compute if operand
                - if +
                    - push sum of 2 terms onto stack
                - if -
                    - secondTerm = popped
                    - fistTerm = popped
                    - push difference onto stack
                - if *
                    - push product of 2 terms onto stack
                - if /
                    - divisor = first element popped
                    - divide = second element popped
                    - push quoteint stack
                
            - push integers to stack
            return sum(stacks)
            
        Time: O(N) to iterate throught tokens and sum stack
        Space: O(N) stack
        
        '''
        stack = []
        for t in tokens:
            # print(t, stack)
            if t.isdigit() or t[1:].isdigit():
                stack.append(int(t))
            else:
                if t == '+':
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first+second)
                elif t == '-':
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first-second)
                elif t == '*':
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first * second)
                else:
                    # division
                    second = stack.pop()
                    first = stack.pop()
                    # handles negative divisor ex: -6 // -132 => 0
                    stack.append(int(first / second))
        return sum(stack)