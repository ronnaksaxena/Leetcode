class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        '''
        clarifiying question:
            - is balanced paranthesis? yes
            - what chars can s contain? '(' or ')'
            - can s be empty? no

        Score:
        - () == 1 (base case)
        - ()() == 1 + 1 => 2
        - ((())) = 1 * 2 * 2 => 4

        Idea: keep score of nested paranthesis in a stack
        - whenever I encounter closing parenthesis compute current score

        '((()()))'
                i

        stack = [8]

        '''
        
        stack = [0] # score at outer most layer

        for p in s:
            if p == '(':
                stack.append(0)
            else:
                layerScore = stack.pop()
                '''
                Layer case:
                () [0, 0] => score of 1 => [1]
                ()() [0, 1] => score of 2 => [2]

                '''
                stack[-1] += layerScore * 2 if layerScore > 0 else 1
        return stack.pop()

    '''
    Time & Space O(N)
    '''
        