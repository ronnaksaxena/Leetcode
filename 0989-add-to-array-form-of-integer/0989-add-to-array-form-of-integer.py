class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        kDigits = [int(d) for d in str(k)]
        output = collections.deque([0 for _ in range(max(len(kDigits),len(num)))])
        
        
        carry = 0
        kPtr = len(kDigits)-1
        i = len(num) -1
        j = len(output) - 1
        while i >= 0 or kPtr >= 0:
            total = (num[i] if i >= 0 else 0) + (kDigits[kPtr] if kPtr >= 0 else 0) + carry
            carry = total// 10
            digit = total%10
            output[j] = digit
            kPtr -= 1
            i -= 1
            j -= 1
        if carry > 0:
            carryDigits = [int(d) for d in str(carry)]
            while carryDigits:
                output.appendleft(carryDigits.pop())
            
        return output
        