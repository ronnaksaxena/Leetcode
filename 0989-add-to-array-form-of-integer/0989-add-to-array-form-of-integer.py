class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        carry = 0
        result = []

        while i >= 0 or k > 0:
            digit1 = num[i] if i >= 0 else 0
            digit2 = k % 10 if k > 0 else 0
            sum = digit1 + digit2 + carry
            carry = sum // 10
            result.append(sum % 10)
            i -= 1
            k //= 10

        if carry > 0:
            result.append(carry)

        result.reverse()
        return result




        