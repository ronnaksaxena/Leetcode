class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        primes = [True for i in range(n)]
        
        count = 0
        
        for i in range(2, floor(sqrt(n)+1)):
            if not primes[i]:
                continue
            
            for j in range(i**2,n,i):
                primes[j] = False
        
        for i in range(2,n):
            if primes[i]:
                count += 1
        
        return count
