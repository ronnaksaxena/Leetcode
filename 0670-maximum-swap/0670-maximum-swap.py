class Solution:
    def maximumSwap(self, num: int) -> int:
        '''
        Want largest digits to right
        Find first digit that is less than elem to right
        
        
        Base case if all nums[i] >= nums[i+1]: already max
        all numbers are nonincreasing
        
        otherwise:
        find first non 9 element: check for greatest element to right
        
        Algo:
        - store last occurance of each digit {digit: index}
        - loop right and if digit is not 9
            - check for greater digit after it
            - if not continue
        Time: O(N) where n is digits in num
        
        '''
        
        digits = [int(d) for d in str(num)]
        lastOccurance = {d: i for i, d in enumerate(digits)}
        for i in range(len(digits)):
            if digits[i] == 9:
                continue
            for j in range(9, digits[i], -1):
                swapIndex = lastOccurance.get(j,-1)
                if i < swapIndex:
                    # We can swap
                    digits[i], digits[swapIndex] = digits[swapIndex], digits[i]
                    return int(''.join([str(d) for d in digits]))
        return num
        
        