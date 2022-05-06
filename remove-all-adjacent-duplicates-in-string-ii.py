class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        counter_stack = []
        for val in s:
            if not stack or stack[-1]!=val:
                stack.append(val)
                counter_stack.append(1)
            elif stack[-1]==val:
                counter_stack[-1]+=1
            if counter_stack[-1]==k:
                counter_stack.pop()
                stack.pop()
        return ''.join([stack[i]*counter_stack[i] for i in range(len(stack))])
                    
        
