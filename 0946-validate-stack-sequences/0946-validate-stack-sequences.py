class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        '''
        pushed = [2, 1, 0]
                     i
        popped = [1, 2, 0]
                  j
        
        stack = [2,]
        '''
        
        ptr = 0
        stack = []
        for i in range(len(pushed)):
            while ptr < len(popped) and stack and stack[-1] == popped[ptr]:
                stack.pop()
                ptr += 1
            stack.append(pushed[i])
        for j in range(ptr, len(popped)):
            # print(stack, popped[j])
            if not stack or stack.pop() != popped[j]:
                return False
        
        return True
            
        