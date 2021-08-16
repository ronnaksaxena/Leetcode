class Solution:
    def numberToWords(self, num: int) -> str:
        under_20 = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen',]
        tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        chunks = ['Thousand','Million','Billion']
        
        def helper(num):
            if num == 0:
                return []
            if num < 20:
                return [under_20[num]]
            if num < 100:
                return [tens[num//10]] + helper(num%10)
            if num < 1000:
                quotient, remainder = num // 100, num % 100
                return [under_20[quotient], 'Hundred'] + helper(remainder)
            else:
                for power, chunk in enumerate(chunks,1):
                    if num < 1000 ** (power+1):
                        quotient, remainder = num // (1000**power), num % (1000**power)
                        return helper(quotient) + [chunk] + helper(remainder)
                    
        return ' '.join(helper(num)) or 'Zero'
