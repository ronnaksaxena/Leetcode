class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        '''
        "456"
         i
          
         "77"
         j
           
         carry = 1
           
        [3, 3]
        
        while i >= 0 and j >= 0:
            enque (sum of values + carry) % 10
            carry += (sum of values + carry) // 10
            
        while i >= 0:
            same operations with elements in num1
        while j >= 0:
            same operations with elements in num2
        while carry:
            enque carry % 10
            carry //= 10
        transform q into integer return it
        '''
        i = len(num1) - 1
        j = len(num2) - 1
        q = collections.deque()
        carry = 0
        # Both have digits left to process
        while i >= 0 and j >= 0:
            digitSum = int(num1[i]) + int(num2[j]) + carry
            # Enque last digit
            q.appendleft(str(digitSum % 10))
            carry = digitSum // 10
            i -= 1
            j -= 1
        # Add remaining values from num 1
        while i >= 0:
            digitSum = int(num1[i]) + carry
            # Enque last digit
            q.appendleft(str(digitSum % 10))
            carry = digitSum // 10
            i -= 1
        # Add remaining values from num 2
        while j >= 0:
            digitSum = int(num2[j]) + carry
            # Enque last digit
            q.appendleft(str(digitSum % 10))
            carry = digitSum // 10
            j -= 1
        # Add rest of carry
        while carry:
            q.appendleft(str(carry%10))
            carry //= 10

        return ''.join(q)
        