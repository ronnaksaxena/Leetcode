class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def rotate(n):
            digits = [d for d in str(n)]
            if digits[-1] == '9':
                newLength = len(digits) + 1
                newDigits = [str(i) for i in range(1, newLength+1)]
                return int(''.join(newDigits))
            else:
                lastDigit = int(digits[-1]) + 1
                firstDigit = int(digits[0]) + 1
                newDigits = [str(i) for i in range(firstDigit, lastDigit+1)]
                return int(''.join(newDigits))
        
        startLength = len(str(low))
        cur = int(''.join([str(i) for i in range(1, startLength+1)]))
        while cur < low:
            cur = rotate(cur)
        output = []
        while low <= cur <= high:
            output.append(cur)
            cur = rotate(cur)
        return output
                
        