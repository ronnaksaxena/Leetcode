class Solution:
    def decodeString(self, s: str) -> str:
        cur_str = ''
        cur_num = 0
        stack = []
        
        for c in s:
            if c.isnumeric():
                cur_num = cur_num*10 + int(c)
            elif c == '[':
                stack.append((cur_str,cur_num))
                cur_str = ''
                cur_num = 0
            elif c == ']':
                popped_str, popped_num = stack.pop()
                cur_str = popped_str + cur_str*popped_num
            else:
                cur_str += c
                
        return cur_str
